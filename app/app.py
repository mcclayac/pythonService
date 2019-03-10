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

from flask import Flask, request, render_template
app = Flask(__name__)
default_key = '1'
cache = {default_key: 'one'}

@app.route('/', methods=['GET', 'POST'])
def mainpage():
    key = default_key
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        cache[key] = request.form['cache_value']

    cache_value = None;
    if key in cache:
        cache_value = cache[key]

    return render_template('index.html', key=key, cache_value=cache_value)


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
