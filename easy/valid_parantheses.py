def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack_n = []
    for x in s:
        if x == '[':
            stack_n.append(']')
            continue
        if x == '{':
            stack_n.append('}')
            continue
        if x == '(':
            stack_n.append(')')
            continue
        if not stack_n or stack_n.pop() != x:
            return False
    return not stack_n


if __name__ == "__main__":
    print(isValid("(){}[]"))
    print(5//2)
