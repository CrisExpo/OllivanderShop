from flask import Flask, render_template
from gilded_rose import GildedRose
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def blog():
    return render_template('index.html')





if '__name__' == '__main__':
    app.run()