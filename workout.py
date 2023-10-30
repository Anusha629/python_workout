def fizzbizz(n):
    for i in range(1,n+1):
        if i % 15 == 0:
            print("fizzbizz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("bizz")
        else:
            print(i)

n=50
fizzbizz(n)


def panagram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()

    for letter in alphabets:
        if letter not in s:
            return False 
    return True

input = "he quick brown fox jumps over the lazy dog"
output = panagram(input)
print(output)


def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input = "dad"
output = palindrome(input)
print(output)
