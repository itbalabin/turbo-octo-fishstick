import os


class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        password = os.getenv('AUTH_PASSWORD')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")


class Environment:
    PROD = 'prod'

    URL = {
        PROD: 'https://stage.skies.land/'
    }

    def __init__(self):
        try:
            self.env = os.getenv('ENV')
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URL:
            return self.URL[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


host = Environment()
