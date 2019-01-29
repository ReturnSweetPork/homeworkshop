from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/dictionary/<string:word>")


def index(word):
    fruit = {
        "apple":"사과",
        "banana":"바나나",
        "orange":"오렌지"
    }
    
    if word in fruit:
        mean = fruit[word]
    else:
        mean = "나만의 단어장에 없음"
    return render_template("dictionary.html",word=word,mean=mean)    
    
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)        