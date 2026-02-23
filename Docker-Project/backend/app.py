from flask import Flask, jsonify,request
from business import get_data
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/api', methods=['GET'])
def api():
    data=get_data()
    
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0', debug=True)