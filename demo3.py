from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template

import sqlite3
from flask import g

app = Flask(__name__)

DATABASE = './test_demo_7.db'
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = get_db().cursor()
    cursor.execute( 'select * from COMPANY' )
    values = cursor.fetchall()
    print(values)
    print( type('runoob') )
    print( type( values ) )
    python2json = {}
    python2json["listData"] = values
    print( type( python2json ) )
    return  str(python2json)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return '<h1>Bad Request</h1>', 400

# @app.route('/session', methods=['GET', 'POST']) 
# def index():
# form = NameForm()
#     if form.validate_on_submit():
#         session['name'] = form.name.data
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'))

@app.route('/form', methods=['GET'])
def form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/user', methods=['GET'])
def user():
    return render_template('./user.html')

@app.route('/wrong')
def wrong():
    return abort(404)

@app.route('/redirect')
def redirect():
    return redirect('www.baidu.com')

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer-11', '4r2')
    response.set_cookie('answer-12', '42rrr')
    response.set_cookie('answer-13', '4rrr2')
    response.set_cookie('answer-14', '4rrrr2')
    response.set_cookie('answer-15', '4r2')
    response.set_cookie('answer-16', '42rrr')
    response.set_cookie('answer-17', '4rrr2')
    response.set_cookie('answer-18', '4rrrr2')
    response.set_cookie('answer-111', '4r2')
    response.set_cookie('answer-112', '42rrr')
    response.set_cookie('answer-113', '4rrr2')
    response.set_cookie('answer-114', '4rrrr2')
    response.set_cookie('answer-115', '4r2')
    response.set_cookie('answer-116', '42rrr')
    response.set_cookie('answer-117', '4rrr2')
    response.set_cookie('answer-118', '4rrrr2')
    response.set_cookie('answer-111', '4r2')
    response.set_cookie('answer-2112', '42rrr')
    response.set_cookie('answer-2113', '4rrr2')
    response.set_cookie('answer-2114', '4rrrr2')
    response.set_cookie('answer-2115', '4r2')
    response.set_cookie('answer-2116', '42rrr')
    response.set_cookie('answer-2117', '4rrr2')
    response.set_cookie('answer-2118', '4rrrr2')
    response.set_cookie('answer-3111', '4r2')
    response.set_cookie('answer-3112', '42rrr')
    response.set_cookie('answer-3113', '4rrr2')
    response.set_cookie('answer-3114', '4rrrr2')
    response.set_cookie('answer-3115', '4r2')
    response.set_cookie('answer-3116', '42rrr')
    response.set_cookie('answer-3117', '4rrr2')
    response.set_cookie('answer-3118', '4rrrr2')
    response.set_cookie('answer-4111', '4r2')
    response.set_cookie('answer-4112', '42rrr')
    response.set_cookie('answer-4113', '4rrr2')
    response.set_cookie('answer-4114', '4rrrr2')
    response.set_cookie('answer-4115', '4r2')
    response.set_cookie('answer-4116', '42rrr')
    response.set_cookie('answer-4117', '4rrr2')
    response.set_cookie('answer-4118', '4rrrr2')
    return response

@app.route('/user_agent',methods=['GET'])
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/name', methods=['GET', 'POST'])
def home():
    return '{"name":"my_name","age":23,"year":2018}'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        print(request.form['username'])
        print(request.form['password'])
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()