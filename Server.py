from flask import Flask
from controller.JobController import post_job


class Server:

    def __init__(self):
        self.app = None

    def start_server(self, config):
        self.app = Flask(__name__)
        self.__define_route()
        self.__run(config)

    def __define_route(self):

        @self.app.route("/postjob", methods=['POST'])
        def post():
            return post_job()

    def __run(self, config):
        self.app.run(host=config["host"], port=config["port"], debug=False)
