#from crypt import methods
from flask import Flask,jsonify,render_template,Response,request


app=Flask(__name__)

@app.route('/')

def home():
    return render_template('add.html')

@app.route('/addition' ,methods=['POST','GET'])
def add():
    if request.method =='POST':
        data = request.get_json('data')
        #print(data)
        val1 = data['val1']
        val2 = data['val2']
        print(val2)
        #print(val1)
        val3=int(val1)+int(val2)
        val3=str(val3)
        return {'response':val3}


if '__name__' == "__main__":
    app.run(debug = True)
