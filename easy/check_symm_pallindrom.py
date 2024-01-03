# symmetrical and palindrome
def check_symmetrical(string_name):
    str = string_name
    if str[0:int((len(str) / 2))] == str[int((len(str) / 2)):]:
        print("symmetrical")
        return True


def check_palindromne(string_name):
    str = string_name
    if str == str[::-1]:
        print("pallindrome")


def main():
    string_name = input("enter name")
    check_symmetrical(string_name)
    check_palindromne(string_name)


if __name__ == "__main__":
    main()