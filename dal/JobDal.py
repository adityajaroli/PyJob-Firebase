from .DbConnection import DbConnection


class JobDal:

    def __init__(self):
        conn = DbConnection.get_connection()
        self.__db = conn.firebase
        self.__token = conn.token

    def get(self):
        data = self.__db.child("<Table_Name>").get(self.__token).val()
        return data

    def insert(self, object_to_insert):
        self.__db.child("<Table_Name>").push(object_to_insert, self.__token)
