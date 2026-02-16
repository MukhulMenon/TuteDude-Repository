from flask import Flask, render_template, request
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def home():
    day_of_week=datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    user=request.values.get('user')
    if not user:
        user='Guest'
    return render_template('index.html',dayOfWeek=day_of_week,currentTime=current_time,user=user)
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