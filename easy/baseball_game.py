"""

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.




Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""
from functools import reduce

def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    stack = []
    x = 0
    for index in range(len(operations)):
        if operations[index] == '+':
            stack.append(stack[len(stack) - 1] + stack[len(stack) - 2])
        elif operations[index] == 'D':
            stack.append(2 * (stack[len(stack) - 1]))
        elif operations[index] == 'C':
            stack.pop()
        else:
            stack.append(int(operations[index]))
    # for elem in stack:
    #     x += elem
    x = reduce(lambda x,y: x+y , stack)
    return x


if __name__ == "__main__":
    score_strategy = ["5","2","C","D","+"]
    print(calPoints(score_strategy))