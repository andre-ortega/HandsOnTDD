# Andre Ortega
# CS362: TDD

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = 'abcdefg' #length 7
        self.assertEqual(check_pwd(input), False)

    def test2(self):
        input = 'aB3defgh-' #length 9, full password
        self.assertEqual(check_pwd(input), True)

    def test3(self):
        input = 'abcdefghijklmnopqrstuv' #length 22
        self.assertEqual(check_pwd(input), False)

    def test4(self):
        input = 'abcdefgh' #length 8, no uppercase letter
        self.assertEqual(check_pwd(input), False)

    def test5(self):
        input = 'ABCDEFGH' # no lowercase letter
        self.assertEqual(check_pwd(input), False)

    def test6(self):
        input = 'Abcdefgh' # no digit
        self.assertEqual(check_pwd(input), False)

    def test7(self):
        input = '1234567' # only digits
        self.assertEqual(check_pwd(input), False)

    def test8(self):
        input = 'A2cdefgh' # No special character
        self.assertEqual(check_pwd(input), False)

    def test9(self):
        input = 'A2cdefghijklmnop~' # No special character
        self.assertEqual(check_pwd(input), True)

    def test10(self):
        input = 'A2lmnp~' # Meets all criteria except length
        self.assertEqual(check_pwd(input), False)

    def test11(self):
        input = '123$56aA' # Meets all criteria
        self.assertEqual(check_pwd(input), True)


if __name__ == '__main__':
    unittest.main()
