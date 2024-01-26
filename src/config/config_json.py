from config_impl import ConfigImpl
import json

class ConfigJson(ConfigImpl):
    def __init__(self):
        super().__init__()

    @staticmethod        
    def write(data, file):
        with open(file, 'w') as f:
            f.write(json.dumps(data, indent=4))
    
    @staticmethod
    def read(file):
        return json.load(open(file, 'r'))