from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from subprocess import Popen, PIPE, TimeoutExpired, CalledProcessError
import shlex

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class CodeForm(FlaskForm):
    code = StringField('code', validators=[InputRequired()])
    timeout = IntegerField('timeout', validators=[InputRequired(), NumberRange(min=1, max=30)])


@app.route('/execute', methods=['POST'])
def execute_code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        try:
            cmd = f'python -c {code}'
            process = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate(timeout=timeout)
            if process.returncode == 0:
                return jsonify({'result': stdout.decode()})
            else:
                return jsonify({'error': stderr.decode()})
        except TimeoutExpired:
            process.kill()
            return jsonify({'error': 'Execution time exceeded'})
        except CalledProcessError as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Invalid input'}), 400


if __name__ == '__main__':
    app.run(debug=True)
