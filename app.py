from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Shiyanlou002!test111111'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)

