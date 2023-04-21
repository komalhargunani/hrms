
import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/Config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'baseurl')
        return url


    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

