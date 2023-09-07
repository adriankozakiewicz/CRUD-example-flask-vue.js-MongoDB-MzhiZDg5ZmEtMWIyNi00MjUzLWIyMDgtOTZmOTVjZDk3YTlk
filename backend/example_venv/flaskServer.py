from AuthController import AuthController
from flask import Flask
import flask
from flask.typing import AppOrBlueprintKey
from apiModule import ApiModule
from frontend import Views
from flask_restful import Api, reqparse
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)



dbClient = MongoClient('localhost', 27017)
authController = AuthController(dbClient)


parser = reqparse.RequestParser()
parser.add_argument('token')

# api
api.add_resource(ApiModule.Notes, '/api/notes/', resource_class_kwargs={ 'db_client': dbClient, 'auth_controller': authController })
api.add_resource(ApiModule.Note, '/api/note/<string:note_id>', resource_class_kwargs={ 'db_client': dbClient, 'auth_controller': authController })
api.add_resource(ApiModule.Login, '/api/login/', resource_class_kwargs={ 'db_client': dbClient, 'auth_controller': authController })
api.add_resource(ApiModule.Register, '/api/register/', resource_class_kwargs={ 'db_client': dbClient, 'auth_controller': authController })
api.add_resource(ApiModule.CheckToken, '/api/checkToken/', resource_class_kwargs={ 'db_client': dbClient, 'auth_controller': authController })


#frontend-holders
#app.add_url_rule('/favicon.ico',redirect_to="/static/favicon.png")
app.add_url_rule('/', view_func=Views.Index.as_view("indexView"))
app.add_url_rule('/dashboard', view_func=Views.Dashboard.as_view("dashboardView"))
app.add_url_rule('/login', view_func=Views.Login.as_view("loginView"))
app.add_url_rule('/register', view_func=Views.Register.as_view("registerView"))


#@app.route('/scripts/<filename>', view_func=views.scripts)
#@app.route('/styles/<filename>', view_func=views.styles)
#@app.route('/assets/<filename>', view_func=views.assets)



def hello_world():
    return 'Hello world!'