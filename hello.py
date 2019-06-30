from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello</h1>"

@app.route('/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)#

# @app.route("/")
# def hello():
#     return render_template("hello.html")

# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user)

    # render_template('hello.html')
# @app.route("/<name>")
# def hello_name(name):
#     return "hello {}".format(name)

if __name__== "__main__":
    app.run()
