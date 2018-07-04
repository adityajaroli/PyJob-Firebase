from Server import Server


class Application:

    config = {
        "host": "localhost",
        "port": 8080
    }

    @staticmethod
    def run():
        Server().start_server(Application.config)


if __name__ == "__main__":
    Application.run()
