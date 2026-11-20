from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, DevOps World! V1"

if __name__ == '__main__':
    app.run()
