import base64
import os


class AppUtil:

    @staticmethod
    def create_file(file_stream, file_name, file_path=None):
        if file_stream is None or file_name is None:
            raise Exception("File_stream or file_name cannot be empty")

        if file_path is not None:
            file_name = file_path+"/"+file_name

        decoded_file = base64.b64decode(file_stream).decode('utf-8')
        file_obj = open(file_name, "w")
        file_obj.write(decoded_file)
        file_obj.close()

        return AppUtil.get_abs_path(file_name)

    @staticmethod
    def get_abs_path(file_name):
        return os.path.abspath(file_name)