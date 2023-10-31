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
    
    
    
def freq(s):
    freq_dict = {}
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    return freq_dict

class TestFreq(unittest.TestCase):

    def testIsFreq(self):
        sentence = "hello galaxy"
        self.assertTrue(freq(sentence))

    def testCaseInsensitive(self):         
         sentence = "Hello GAlaxy"
         self.assertTrue(freq(sentence))

    def testEmptyInput(self):
        ret = freq("")
        self.assertFalse(ret)
        

if __name__ == '__main__':
    unittest.main()

