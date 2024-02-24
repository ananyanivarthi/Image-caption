from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return 'Hello World'

@app.route('/index',methods=['GET'])
def index1():
    return 'Hello World2'    

if __name__ == '__main__':
    app.run(port=3000,debug=True)
