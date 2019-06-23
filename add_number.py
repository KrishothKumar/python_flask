from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

@app.route('/')
def input_input():
        return render_template('input.html')

@app.route('/add', methods=['POST'])
def user_input():
        user1 = int(request.form['finput'])
        user2 = int(request.form['linput'])
        user1 = user1 + user2
        return redirect(url_for('result_display', name = user1))

@app.route('/add/<name>')
def result_display(name):
    return "Result: {}".format(name)
#
# def user_input():
#     user1 = r

if __name__=="__main__":
    app.run()
