from .DbConnection import DbConnection


class Dal:

    def __init__(self):
        conn = DbConnection.get_connection()
        self.__db = conn.firebase
        self.__token = conn.token

    def get(self, table_name):
        data = self.__db.child(table_name).get(self.__token).val()
        return data

    def insert(self, table_name, object_to_insert):
        self.__db.child(table_name).push(object_to_insert, self.__token)
