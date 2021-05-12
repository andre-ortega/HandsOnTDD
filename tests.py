import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = 'aaaaaaa' #length 7
        self.assertEqual(check_pwd(input), False)

    def test2(self):
        input = 'aaaaaaaa' #length 8
        self.assertEqual(check_pwd(input), True)


if __name__ == '__main__':
    unittest.main()
