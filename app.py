from flask import Flask,request,render_template

app = Flask(__name__)


@app.route("/")
def home():
   return render_template('add.html')

@app.route('/add')
def adder():
    a=request.args.get('a','')
    b=request.args.get('b','')
    
    a=int(a)
    b=int(b)
    

    result=a+b
    return render_template('result.html',result=result)




@app.route('/min')
def  minus():
    c=request.args.get('c','')
    d=request.args.get('d','')
    
    c=int(c)
    d=int(d)
    
    return f'minus : {c-d}'
if __name__ == "__main__":
    app.run(port=4200, debug=True)
