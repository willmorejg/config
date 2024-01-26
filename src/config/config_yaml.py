from config_impl import ConfigImpl
import yaml

class ConfigYaml(ConfigImpl):
    def __init__(self):
        super().__init__()

    @staticmethod        
    def write(data, file):
        yaml.dump(data, open(file, 'w'))
    
    @staticmethod
    def read(file):
        return yaml.load(open(file, 'r'), Loader=yaml.FullLoader)
