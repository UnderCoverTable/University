def Palindrome(str):
    if len(str) < 2:
        return True

    else:

        if str[0] == str[len(str) - 1]:
            return Palindrome(str[1:-1])
        else:
            return False


print(Palindrome("ca"))
