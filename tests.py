import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = 'abcdefg' #length 7
        self.assertEqual(check_pwd(input), False)

    def test2(self):
        input = 'abcdefgh' #length 8
        self.assertEqual(check_pwd(input), True)

    def test3(self):
        input = 'abcdefghijklmnopqrstuv' #length 22
        self.assertEqual(check_pwd(input), False)

if __name__ == '__main__':
    unittest.main()
