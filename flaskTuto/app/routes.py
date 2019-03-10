# the routes are the different URL's that the appl implements. 
# Handlers for the appl routes are written as py functions, called view functions

from app import app


# these two @app.route lines are decorators, which modify the function that follows it
# We can use them to register functions as callbacks for certain events. 
# Here it creates an association between the URL given as an argument and the function
# When a browser requests either fo these two URLs, flask will invoke the function and pas the return value back to the browser
@app.route('/')
@app.route('/index')
@app.route('/hello')
def index():
    return "Hello World, this is Joris!"
