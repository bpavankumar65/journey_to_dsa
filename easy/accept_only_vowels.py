def accept_vowels(string_var):
    str_var = set(string_var)
    set_vowel = {'a','e','i','o','u'}
    if set_vowel & str_var == set_vowel:
        print("yes")

if __name__ == "__main__":
    string_var = "pavanBandaruisgoodie "
    accept_vowels(string_var)