# the application will exist in a package, which for python is a subdirectory that includes a __init__.py file. 


# this script creates the application object as an instance of class Flask. 
from flask import Flask
# __name__ is a python predifined var, which is set to the name of the module in which it is used
# this should almost always configure flask correctly
app = Flask(__name__)
# routes does not exist yet
# routes is imported at the end of the script. This is a workaround for circular imports, common issue with flask applications
from app import routes