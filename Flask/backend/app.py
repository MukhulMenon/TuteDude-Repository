import os
from flask import Flask,request
import pymongo

uri = os.getenv('MONGOURI')  # Replace with your MongoDB connection string

# Create a new client and connect to the server
client = pymongo.mongo_client.MongoClient(uri)
db=client.textdb
collection = db['learning']

app=Flask(__name__)

@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.json)
    collection.insert_one(form_data)
    return 'Data submitted successfully'

@app.route('/view')
def view():
    data=list(collection.find())
    data=[{'name':item['fullname'],'age':item['age'],'country':item['country'],'userName':item['username']} for item in data]
    data={
        'data':data
    }
    return data
if __name__=='__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)