import os
from flask import Flask,request
import pymongo

uri = os.getenv('MONGOURI')  # Replace with your MongoDB connection string

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)
db=client.textdb
collection = db['learning']

app=Flask(__name__)

@app.route('/')
def home():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return ("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        return ({"error": str(e)}), 400

@app.route('/submit',methods=['POST'])
def submit():
    try:
        form_data=dict(request.json)
        collection.insert_one(form_data)
        return 'Data submitted successfully' ,200
    except Exception as e:
        return ({"error": str(e)}), 400
    

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