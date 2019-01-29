from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
    
@app.route("/dic/<string:word>")
def index(word):
    fruit = {
        "apple" : "사과",
        "banana" : "바나나"
    }
    
    if word in fruit:
        mean = fruit[word]
    else:
        mean = "나만의 단어장에 있지 않습니다."
    return render_template("dic.html", word = word, mean = mean)
    
    

@app.route("/dic/<string:word>")
def dic(word):
    mydic = {
        "apple" : "사과",
        "banana" : "바나나"
    }
    result = mydic.get(word)
    if result:
        result = f"{word} : {result}"
    else:
        result = f"{word}는 단어장에 없는단어 입니다"
    
    return reslt
    
    
@app.route("/workshop")
def workshop():
    return render_template("workshop.html")
    
    
@app.route("/workshop2")
def workshop2():
    return render_template("workshop2.html")
    
    
    
    
    
        
if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)