from flask import Flask, request

app = Flask(__name__)

@app.route('/post_logs', methods = ["POST"])
def post_logs():
    data = request.form.to_dict()
    with open("./logs.log", 'a+') as f:
        log = f'{data["levelname"]} | {data["name"]} | {data["lineno"]} | {data["msg"]}\n'
        f.write(log)

@app.route('/get_logs', methods = ["GET"])
def get_logs():
    with open('./logs.log', 'r') as f:
        return f"<pre>{f.read()}</pre>"

if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
