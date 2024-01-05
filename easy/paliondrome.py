import re

def is_palindrome(x):
    reverse = 0
    temp = x
    while temp > 0:
        rem = temp % 10
        reverse = reverse * 10 + rem
        temp = temp / 10
    if x == reverse:
        return True
    else:
        return False


def is_palindrome_string(x):
    if x / 10 == 0:
        return True
    str_var = str(x)
    if str_var == str_var[::-1]:
        return True
    else:
        return False

#not recommended
def isPalindrome(s: str):
    """
    :type s: str
    :rtype: bool
    """
    x = re.split(r'[,?.|\-#@:\'\"`~!$%^*({}/\[/\]/)_; ]', s)
    string_s = ""
    for elem in x:
        string_s += elem
    string_s = string_s.lower()
    if string_s == string_s[::-1]:
        return True
    else:
        return False

# lets try
def is_palindrom_delimiter(s):
    s.split(" ")
    string_var = ''
    for elem in s:
        if elem.isalnum():
            string_var += elem
    string_var = string_var.lower()
    if string_var == string_var[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome_string(121))
    print(is_palindrome(101))
    print(isPalindrome("heeh . ? "))
    print(is_palindrom_delimiter("heeh ... ?"))
