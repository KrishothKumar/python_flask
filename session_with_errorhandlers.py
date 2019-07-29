from flask import Flask, request, url_for, redirect, render_template,make_response,session,escape
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.errorhandler(404) # This handler is used to avoid errors on the page
def page_not_found(error):
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# @app.errorhandler(404) # This handler is used to avoid errors on the page
# def page_not_found(error):
#     return render_template('hello.html')

# @app.errorhandler(404)
# def not_found(error):
#     resp = make_response(render_template('hello.html'), 404)
#     resp.headers['X-Something'] = 'A value'
#     return resp
#
# @app.route('/ss')
# def input_input():
#         resp = make_response(render_template('input.html'))
#         resp.set_cookie('finput', 'user_value1')
#         resp.set_cookie('linput', 'user_value2')
#         return resp
#
# @app.route('/add', methods=['POST'])
# def user_input():
#         user1 = int(request.form['finput'])
#         user2 = int(request.form['linput'])
#         user1 = user1 + user2
#         return redirect(url_for('result_display', name = user1))
#
# @app.route('/add/<name>')
# def result_display(name):
#     return "Result: {}".format(name)
#
# def user_input():
#     user1 = r

# if __name__=="__main__":
#     # app.config['DEBUG'] = True
#     app.run()
