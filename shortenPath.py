"""
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes 
such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

    It must start with a single slash '/'.
    Directories within the path should be separated by only one slash '/'.
    It should not end with a slash '/', unless it's the root directory.
    It should exclude any single or double periods used to denote current or parent directories.

Return the new path.
"""

"""
In case you are given an absolute path, use this:

def simplifyPath(path):
    tokens = filter(isImportantToken, path.split("/"))
    stack = [""]
    for token in tokens:
        if token == ".." and stack[-1] != "":
            stack.pop()
        elif token != "..":
            stack.append(token)
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)


def isImportantToken(token):
    return len(token) > 0 and token != "."

"""

def simplifyPath(path):
    startsWithSlash = path[0] == "/"
    tokens = filter(isImportantToken, path.split("/"))  # First time I use the filter function, it's cool to know. If it doesn't fulfills the condition it's filtered
    stack = []                                          # If it's difficult to work with your list, just use another one as a container
    if startsWithSlash:
        stack.append("")
    for token in tokens:
        if token == "..":
            if len(stack) == 0 or stack[-1] == "..":    # Either way you're working with a relative path
                stack.append(token)
            elif stack[-1] != "":                       # This applies only to absolute paths
                stack.pop()
        else:
            stack.append(token)
    if len(stack) == 1 and stack[0] == "":
        return "/"
    return "/".join(stack)



def isImportantToken(token):
    return len(token) > 0 and token != "."

path = "/foo/../test/../test/../foo//bar/./baz"
print(simplifyPath(path))
