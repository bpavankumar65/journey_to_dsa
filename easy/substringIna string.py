def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    length = len(needle)
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i:i + length] == needle:
                return i
    return -1


if __name__ == "__main__":
    strStr("subwaysaab", "sub")