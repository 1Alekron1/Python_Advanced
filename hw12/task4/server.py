from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/timestamp/<timestamp>')
def get_timestamp(timestamp: str) -> str:
    timestamp = float(timestamp)
    return str(datetime.fromtimestamp(timestamp))

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)
