from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD Pipeline is a massive success! V2"

if __name__ == '__main__':
    app.run()
