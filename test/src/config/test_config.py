import unittest 
import os
import sys  

base_dir = os.path.normpath(os.getcwd()).split(os.sep)[:-3]

pkg_dir = base_dir.copy()
pkg_dir.append('src')
pkg_dir.append('config')
sys.path.append(os.sep.join(pkg_dir))

test_dir = base_dir.copy()
test_dir.append('test')
test_dir.append('resources')
test_resources_dir = os.sep.join(test_dir)

from config import Config

class Testing(unittest.TestCase):
    def test_init(self):
        config = Config(cfg_path=test_resources_dir)
        self.assertIsNotNone(config)
        print(config)
        config.add_value('test', 'test')
        config.write_file()
        config.read_file()
        self.assertEqual(config.get_value('test'), 'test')


if __name__ == '__main__':
    unittest.main()