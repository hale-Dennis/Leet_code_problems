# Given an integer x, return true if x is a palindrome, and false otherwise

x = 122

def isPalindrome(num):
    string = str(num)
    if string == string[::-1]:
        return True
    return False

if isPalindrome(x):
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")
    

