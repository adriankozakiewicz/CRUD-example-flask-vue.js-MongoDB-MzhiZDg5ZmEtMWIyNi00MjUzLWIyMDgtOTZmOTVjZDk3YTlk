from typing import Tuple
import uuid
from bson import ObjectId

class AuthController:

    #tokenDict = dict()
    #dbClient = None
    cmd_login = ""

    def __init__(self, dbClient):
        self.dbClient = dbClient
        self.tokenDict = dict()


    def checkToken(self, token):
        if self.tokenDict.has_key(token):
            return True
        else: 
            return False


    def getUser(self, token):
        if self.checkToken(token):
            return self.tokenDict[token]
        else:
            return None


    def login(self, user, password):

        users_result = self.dbClient["flask-example"].users.count_documents({ 'username': user, 'password': password })
        try:
            if users_result > 0:
                new_token = self.generateToken(user)
                return (1, new_token)
            else:
                return (2, None)
        except:
            return (3, None)


    def register(self, user, password):

        users_result = self.dbClient["flask-example"].users.count_documents({ 'username': user })
        try:
            if users_result > 0:
                return (2, None) #user already exist
            else:
                self.dbClient["flask-example"].users.insert_one({ 'username': user, 'password': password})
                new_token = self.generateToken(user)
                return (1, new_token)
        except:
            return(3, None)
    
    def checkToken(self, token):

        if token in self.tokenDict.keys():
            return True
        else:
            return False

        
    def generateToken(self, user):
        new_token = uuid.uuid4().hex
        self.tokenDict[new_token] = user
        return new_token






        

