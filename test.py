import unittest

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

if __name__ == '__main__':
    unittest.main()
    
    
