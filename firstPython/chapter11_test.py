import unittest
from chapter11 import get_formatted_name

class NameTest(unittest.TestCase):
    def test_get_formatted_name(self):
        formatted_name= get_formatted_name('dfd', 'bbb')
        self.assertEqual(formatted_name, 'Dfd Bbb')

if __name__ == '__main__':
    unittest.main()