from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)