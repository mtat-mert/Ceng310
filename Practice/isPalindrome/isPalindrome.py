


def isPalindrome(s):
    if len(s)<=1:
        return True
    return s[0]==s[-1] and isPalindrome(s[1:-1])

given_str = ""
while(given_str != '0'):
    print("Give a string to check if it is palindrome 0 to exit.")
    given_str = input().strip("\n")
    print(isPalindrome(given_str))