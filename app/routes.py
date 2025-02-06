from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Justin'}
    posts = [
        {
            'author' : {'username' : 'Amberly'},
            'body' : 'Beautiful day in Jordan!'
        },
        {
            'author' : {'username' : 'Ian'},
            'body' : 'Blockchain is the future!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)