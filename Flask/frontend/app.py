from flask import Flask, render_template, request
from datetime import datetime
import requests


BACKEND_URL='http://0.0.0.0:9000'
app=Flask(__name__)

@app.route('/')
def home():
    day_of_week=datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    user=request.values.get('user')
    if not user:
        user='Guest'
    return render_template('index.html',dayOfWeek=day_of_week,currentTime=current_time,user=user)

@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
    response=requests.post(f'{BACKEND_URL}/submit',json=form_data)
    return f'Data submitted successfully. Response status: {response.status_code}'
           
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)