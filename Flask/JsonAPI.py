from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello Guys"
@app.route('/user')
def user():
    name=request.values.get('name')
    age=int(request.values.get('age'))
    result={
        'name':name,
        'age':age
    }
    return result
if __name__=='__main__':
    app.run(debug=True)