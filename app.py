from flask import Flask
app=Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'

@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>hello, %s!</h1>'% name

if __name__=="__main__":
    app.run()


