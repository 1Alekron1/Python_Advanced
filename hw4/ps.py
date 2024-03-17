from flask import Flask, request
import subprocess
import shlex

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def ps():
    try:
        args = request.args.getlist('arg')
        cmd = ['ps'] + args
        result = subprocess.run(cmd, capture_output=True, text=True)
        formatted_result = shlex.quote(result.stdout)
        return f"<pre>{formatted_result}</pre>"
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
