from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def uptime():
    try:
        result = subprocess.run(['uptime'], capture_output=True, text=True)
        uptime_info = result.stdout.split(',')[0].split('up ')[-1]
        return f"Current uptime is {uptime_info}"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
