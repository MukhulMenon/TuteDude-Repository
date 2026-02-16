from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello Guys"
@app.route('/about')
def about():
    return "This is about page"
@app.route('/contact')
def contact():
    return "Mukhul Menon"
@app.route('/user/<name>')
def user(name):
    print(name)
    length =len(name)
    if(length>5):
        return "welcome to the page "+name+"!"
    else:
        return "ohh no name is too short"

if __name__=='__main__':
    app.run(debug=True)