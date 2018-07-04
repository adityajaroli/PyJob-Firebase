from .Dal import Dal


class JobDal:

    def __init__(self):
        self.dal = Dal()

    def get(self):
        data = self.dal.get("<table_name>")
        return data

    def insert(self, object_to_insert):
        self.dal.insert("<table_name>", object_to_insert)
