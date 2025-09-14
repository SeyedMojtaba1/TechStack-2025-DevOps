from flask import Flask

app = Flask(__name__)

@app.route('/')
def handle():
    return "Hello from Semir! From port 3000."

if "__main__" == __name__:
    app.run(port=3000)
