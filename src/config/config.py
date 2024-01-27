from dataclasses import dataclass, field
from enum import Enum
import os

from config_format_mixin import ConfigFormatMixin
from config_yaml import ConfigYaml
from config_json import ConfigJson
    
class ConfigFormat(ConfigFormatMixin, Enum):
    YAML = ('yaml', 'yml', ConfigYaml)
    JSON = ('json', 'json', ConfigJson)
    
    @staticmethod
    def by_value(value):
        return [item for item in ConfigFormat if item.value.format_id == value]

@dataclass
class Config():
    cfg_path: str = os.path.join(os.path.dirname(__file__), '')
    cfg_filename: str = field(default='config', init=True)
    cfg_format: str = field(default='yaml', init=True)
    cfg_extension: str = field(default='', init=True)
    _cfg_dict: dict = field(default_factory=dict, init=True)
        
    def __getattribute__(self, __name):
        if __name == 'cfg_file':
            return os.path.join(self.cfg_path, self.cfg_filename + '.' + (self.cfg_extension if self.cfg_extension else self._cfg_format[0].extension))
        else:
            return super().__getattribute__(__name)
    
    def __setattr__(self, __name, __value):
        if __name == 'cfg_format':
            self._cfg_format = ConfigFormat.by_value(__value)
        else:
            super().__setattr__(__name, __value)
    
    def add_value(self, key, value):
        self._cfg_dict[key] = value
    
    def get_value(self, key=None):
        if key is None:
            return self._cfg_dict
        return self._cfg_dict[key]
    
    def write_file(self):
        self._cfg_format[0].library.write(data=self._cfg_dict, file=self.cfg_file)
    
    def read_file(self):
        self._cfg_dict = self._cfg_format[0].library.read(file=self.cfg_file)

##test stub
if __name__ == "__main__":
    # instantiate config
    config = Config(cfg_path=os.path.join(os.sep,'home','jim','python','config','test','resources'))
    
    # add values
    config.add_value('test', 'test')
    config.add_value('testAry', ["test XXX", "test YYY"])
    config.add_value('testDict', {"key": "value"})
    config.add_value('new_section', {"foo": {"key": "value"}})
    template = """
                hello world {name}
                this is some text
                signed,
                {author}
                """
    config.add_value('template', template.strip())
    config.add_value('url', 'http://localhost:8080/')

    # print config object
    print(config.__repr__, config._cfg_format, config.cfg_file)

    # change the config format
    config.cfg_format = 'json'
    
    # print config object
    print(config.__repr__, config._cfg_format, config.cfg_file)

    # print config values
    print("test: ", config.get_value('test'))
    print("testAry", config.get_value('testAry'))
    print("values: ", config.get_value())

    # write config file    
    config.write_file()
    
    # read config file
    config.read_file()
    
    # print config values
    print("configuration dict:", config.get_value())
    print("configuration dict - testDict -> key:", config.get_value("testDict").get("key"))
    print("configuration dict - test:", config.get_value("test"))
    
    # example of using a template configuration value
    print(config.get_value("template").format(name="Jim", author="JIMMY"))
