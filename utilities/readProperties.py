import configparser
from pathlib import Path
config=configparser.RawConfigParser()
config_folder=Path("./configirations")
config_file=config_folder/"config.ini"
config.read(config_file)
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        print(f'config file path is {config_file}')
        url=config.get('common info','baseURL')
        return url