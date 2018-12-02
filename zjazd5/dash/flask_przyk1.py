from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    return "xxxx"

@app.route("/y")
def hello2():
    return "yyyy"


if __name__=='__main__':
    app.run()
