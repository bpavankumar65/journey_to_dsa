def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    flag = False
    for i in range(len(s)):
        if s[i] in roman_dict:
            if (i + 1) < len(s):
                if (s[i] + s[i + 1]) in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                    added_val = roman_dict[s[i + 1]] - roman_dict[s[i]]
                    sum += added_val
                    flag = True
                    continue
            if not flag:
                sum += roman_dict[s[i]]
            flag = False
    return sum

# recommended

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s) - 2):
        if roman_dict[s[i + 1]] > roman_dict[s[i]]:
            result -= roman_dict[s[i]]
        else:
            result += roman_dict[s[i]]
    return result + roman_dict[s[-1]]


romanToInt("LMC")
print(roman_to_int("MCMI"))
