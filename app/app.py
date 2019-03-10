"""
        
   created: mcclayac
   Company Name : BigMAN Software
   MyName: Tony McClay
   date: 2019-03-10
   day of month: 10
   
   Project Name: dockerapp
   filename:  app.py
   package name: 
   IDE: PyCharm
   
   
"""

from flask import Flask
app = Flask(__name__)
# app = Flask(__name__)

# from flask import Flask
# app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route('/')
def hello_world():
    return 'Hello, These Nutz'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
