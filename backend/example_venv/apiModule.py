from AuthController import AuthController
from flask_restful import Resource, reqparse

import bson.objectid 
import bson.json_util

import datetime

#api module

class ApiModule:


    class Note(Resource): 

        #dbClient = None
        #authController = None
        #parser = None

        def __init__(self, **kwargs):
            self.putParser = reqparse.RequestParser()
            self.getDeleteParser = reqparse.RequestParser()

            self.getDeleteParser.add_argument("token", location='cookies')

            self.putParser.add_argument("token", location='cookies')
            self.putParser.add_argument("title")
            self.putParser.add_argument("content")

            self.dbClient = kwargs['db_client']
            self.authController = kwargs['auth_controller']

        def get(self, note_id):
            args = self.getDeleteParser.parse_args()

            status_str = 'not available'
            data_obj = None

            #try:
            user = self.authController.getUser(args["token"])
            user_id = self.dbClient["flask-example"].users.find_one({'username':user})["_id"]
            note_db_parser = self.dbClient["flask-example"].notes.find_one({'user_id':bson.objectid.ObjectId(user_id), '_id':bson.objectid.ObjectId(note_id)})

            
            
            note = {
                'id':str(note_db_parser["_id"]), 
                'title':note_db_parser["title"], 
                'content':note_db_parser["content"],
                'last_update':note_db_parser["last_update"].strftime("%m/%d/%Y, %H:%M:%S")
            }

            status_str = 'available'
            data_obj = {'username':user, 'note':note}
            #except Exception as e:
            #    print(e)

            return {'status': status_str, 'data':data_obj}

            

        def put(self, note_id):
            args = self.putParser.parse_args()

            status_str = 'not available'
            data_obj = None

            #try:
            user = self.authController.getUser(args["token"])
            user_id = self.dbClient["flask-example"].users.find_one({'username':user})["_id"]

            updateQuery = {
                'user_id': bson.objectid.ObjectId(user_id),
                '_id': bson.objectid.ObjectId(note_id)
            }

            updatePipeline = {
                '$set': {
                    'title': args["title"],
                    'content': args["content"],
                    'last_update': datetime.datetime.now(tz=datetime.timezone.utc)
                }
            }

            update_result = self.dbClient["flask-example"].notes.update_one(updateQuery, updatePipeline)
            if update_result.matched_count > 0:
                return None, 204
            else: 
                return None, 400
            #except Exception as e:
            #    print(e)
            #    return 403

            

        def delete(self, note_id):
            args = self.getDeleteParser.parse_args()


            #try:
            user = self.authController.getUser(args["token"])
            user_id = self.dbClient["flask-example"].users.find_one({'username':user})["_id"]

            deleteQuery = {
                'user_id': bson.objectid.ObjectId(user_id),
                '_id': bson.objectid.ObjectId(note_id)
            }

            delete_result = self.dbClient["flask-example"].notes.delete_one(deleteQuery)
            if delete_result.deleted_count > 0:
                return None, 204
            else: 
                return None, 400

    class Notes(Resource): 

        #dbClient = None
        #authController = None
        #parser = None

        cmd_get = ""

        def __init__(self, **kwargs):
            self.getParser = reqparse.RequestParser()
            self.postParser = reqparse.RequestParser()

            self.getParser.add_argument("token", location='cookies')

            self.postParser.add_argument("token", location='cookies')
            self.postParser.add_argument("title")
            self.postParser.add_argument("content")

            self.dbClient = kwargs['db_client']
            self.authController = kwargs['auth_controller']

        def get(self):
            args = self.getParser.parse_args()

            status_str = 'not available'
            data_obj = None

            #try:
            user = self.authController.getUser(args["token"])
            _id = self.dbClient["flask-example"].users.find_one({'username':user})["_id"]
            notes_db_parser = self.dbClient["flask-example"].notes.find({'user_id':bson.objectid.ObjectId(_id)})

            note_list = []
            for note_db_obj in notes_db_parser:
            
                note = {
                    'id':str(note_db_obj["_id"]), 
                    'title':note_db_obj["title"], 
                    'last_update':note_db_obj["last_update"].strftime("%m/%d/%Y, %H:%M:%S")
                }
                note_list.append(note)

            status_str = 'available'
            data_obj = {'username':user, 'notes':note_list}
            #except Exception as e:
            #    print(e)

            return {'status': status_str, 'data':data_obj}

        def post(self):
            args = self.postParser.parse_args()


            #try:
            user = self.authController.getUser(args["token"])
            user_id = self.dbClient["flask-example"].users.find_one({'username':user})["_id"]

            insertObject = {
                'title': args["title"],
                'content': args["content"],
                'last_update': datetime.datetime.now(tz=datetime.timezone.utc),
                'user_id': bson.objectid.ObjectId(user_id)
            }

            insert_one_result = self.dbClient["flask-example"].notes.insert_one(insertObject)
            if insert_one_result.acknowledged:
                return None, 204
            else: 
                return None, 400




    class Login(Resource): 

        #dbClient = None
        #authController = None
        #parser = None

        cmd_get = ""

        def __init__(self, **kwargs):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument("login")
            self.parser.add_argument("password")

            self.dbClient = kwargs['db_client']
            self.authController = kwargs['auth_controller']

        def post(self):
            args = self.parser.parse_args()
            

            (status, token) = self.authController.login(args["login"], args["password"])

            #default
            data_obj = None
            status_str = "error: " + str(status)

            #success
            if status == 1:
                data_obj = {'token': token}
                status_str = "logged"
            return {'status': status_str, 'data': data_obj}



    class Register(Resource): 

        #dbClient = None
        #authController = None
        #parser = None

        def __init__(self, **kwargs):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument("login")
            self.parser.add_argument("password")

            self.dbClient = kwargs['db_client']
            self.authController = kwargs['auth_controller']

        def post(self):
            args = self.parser.parse_args()
            

            (status, token) = self.authController.register(args["login"], args["password"])


            #default
            data_obj = None
            status_str = "error: " + str(status)
            
            #success
            if(status == 1):
                token = "sth"
                data_obj = {'token': token}
                status_str = "registered"
            return {'status': status_str, 'data': data_obj}



    class CheckToken(Resource): 

        #dbClient = None
        #authController = None
        #parser = None


        def __init__(self, **kwargs):
            self.parser = reqparse.RequestParser()
            self.parser.add_argument("token")

            self.dbClient = kwargs['db_client']
            self.authController = kwargs['auth_controller']

        def post(self):
            args = self.parser.parse_args()
            
            

            available = self.authController.checkToken(args["token"])


            #default
            data_obj = None
            status_str = "not available"
            
            #success
            if(available == 1):
                status_str = "available"

            return {'status': status_str, 'data': data_obj}