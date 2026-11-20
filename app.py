from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Hello, DevOps World! V1"

if __name__ == '__main__':
    app.run()
