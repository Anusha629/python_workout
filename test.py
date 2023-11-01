import unittest
from workout import palindrome, freq

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def testIsPalindrome(self):
        sentence = "dad"
        self.assertTrue(palindrome(sentence))

    def testIsNotPalindrome(self):
        sentence = "hello"
        self.assertFalse(palindrome(sentence))
    
    def testEmptyInput(self):
        ret = palindrome("")
        self.assertTrue(ret)  



class TestforFreq(unittest.TestCase):
    def testCharacters(self):
        string = "hello"
        expected_string = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(expected_string, freq(string))



if __name__ == '__main__':
    unittest.main()
