import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """
    测试name_function.py
    """

    def test_first_last_name(self):
        """
        能够正确地处理像Stephen Ross这样的姓名吗？
        :return:
        """
        formatted_name = get_formatted_name('stephen', 'ross')
        self.assertEqual(formatted_name, 'Stephen Ross')

    def test_first_middle_last_name(self):
        """
        能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？
        :return:
        """
        formatted_name = get_formatted_name('Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
