from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
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