from pyrebase import pyrebase


class DbConnection:

    __instance = None

    def __init__(self):
        if DbConnection.__instance is not None:
            raise Exception("Singleton class cannot be instantiated directly")
        else:
            self.config = {
                "apiKey": "apiKey",
                "authDomain": "projectId.firebaseapp.com",
                "databaseURL": "https://databaseName.firebaseio.com",
                "storageBucket": "projectId.appspot.com",
                "serviceAccount": "path/to/serviceAccountCredentials.json"
            }
            self.firebase = None
            self.user = None
            self.token = None
            DbConnection.__instance = self

    @staticmethod
    def get_connection():
        if DbConnection.__instance is None:
            DbConnection()
        return DbConnection.__instance

    def connect(self):
        self.firebase = pyrebase.initialize_app(self.config)
        self.__auth()

    def __auth(self):
        auth = self.firebase.auth()
        # authenticate a user
        self.user = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")
        self.token = self.user['idToken']