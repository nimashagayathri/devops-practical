from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<path:path>')
def home(path=""):
    return "CI/CD Pipeline is a massive success! V2"

if __name__ == '__main__':
    app.run()
