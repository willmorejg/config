from config_impl import ConfigImpl
import configparser

class ConfigIni(ConfigImpl):
    def __init__(self):
        super().__init__()

    @staticmethod        
    def write(data, file):
        file_obj = open(file, 'w')
        config_object = configparser.RawConfigParser()
        
        for section, options in data.items():
            print(section, options, type(options))
            if options is not None and isinstance(options, dict):
                config_object.add_section(section)
                for key, value in options.items():
                    config_object.set(section, key, str(value))
            else:
                config_object.set(None, section, str(options))
        
        config_object.write(file_obj)
        file_obj.close()
    
    @staticmethod
    def read(file):
        config_object = configparser.RawConfigParser()
        config_object.read(file)
        data = {}
        for section in config_object.sections():
            data[section] = {}
            for key, value in config_object.items(section):
                data[section][key] = value
        return data