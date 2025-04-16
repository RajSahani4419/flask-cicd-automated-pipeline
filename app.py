from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Backend Running on EC2! Test CI/CD Pipeline Update"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
