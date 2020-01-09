from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello world!</h1>"

@app.route('/blog')
def blog():
    return "<h1>this is a Blog!</h1>"

@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return "this is a Blog number " + str(blog_id)

@app.route('/about')
def about():
    return "<h1>Know more about us</h1>"


if '__name__' == '__main__':
    app.run()