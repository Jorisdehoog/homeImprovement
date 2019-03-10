# the routes are the different URL's that the appl implements. 
# Handlers for the appl routes are written as py functions, called view functions

from flask import render_template
from app import app


# these two @app.route lines are decorators, which modify the function that follows it
# We can use them to register functions as callbacks for certain events. 
# Here it creates an association between the URL given as an argument and the function
# When a browser requests either fo these two URLs, flask will invoke the function and pas the return value back to the browser
@app.route('/')
@app.route('/index')
@app.route('/hello')
def index():
    # create a fake user and some posts
    user = {'username': 'Joris'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Joris'},
            'body': 'Is this the right tutorial for me?'
        },
        {
            'author': {'username': 'Joris'},
            'body': 'I mean it could be if I would want to redo my website'
        }
    ]


    return render_template('index.html', title='Home', user = user, posts = posts)