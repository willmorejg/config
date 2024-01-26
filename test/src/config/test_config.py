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
        # instaniate config
        config = Config(cfg_path=test_resources_dir, cfg_filename='test_config', cfg_format='json')
        self.assertIsNotNone(config)

        # add single value
        config.add_value('test', 'test')

        # add array of values
        ary = ['bing', 'bang', 'bong']
        config.add_value('boom', ary)

        # add a dict of values
        dict = {'bing': 'bang', 'bong': 'boom'}
        config.add_value('dict', dict)
        
        # add nested values
        nested_ary = ['bing', 'bang', 'bong']
        nested_dict = {'bing': 'bang', 'bong': 'boom'}
        nested = {'nested_ary': nested_ary, 'nested_dict': nested_dict}
        config.add_value('nested', nested)

        # write to file        
        config.write_file()
        
        # read from file
        config.read_file()
        
        # test values
        self.assertEqual(config.get_value('test'), 'test')
        self.assertEqual(config.get_value('boom'), ary)
        self.assertEqual(config.get_value('dict'), dict)
        self.assertEqual(config.get_value('nested'), nested)
        self.assertEqual(config.get_value('nested')['nested_ary'][2], nested_ary[2])
        self.assertEqual(config.get_value('nested')['nested_dict']['bong'], nested_dict['bong'])


if __name__ == '__main__':
    unittest.main()