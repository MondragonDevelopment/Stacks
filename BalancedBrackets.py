"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

def validBrackets(string):
    closingBrackets = {")" : "(", "]" : "[", "}" : "{"}
    openingBrackets = []
    if len(string)%2 == 1:
        return False
    for char in string:
        if char in closingBrackets:
            if len(openingBrackets) and openingBrackets[-1] == closingBrackets[char]:
                openingBrackets.pop()
            else:
                return False
        else:
            openingBrackets.append(char)
    return len(openingBrackets) == 0


string = "()[]"
print(validBrackets(string))

