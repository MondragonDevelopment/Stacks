"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

def largestRectangleArea(heights):
    maxArea = 0
    stack = []
    for i, h  in enumerate(heights):                    # Next time I need to keep track of both index and value I must use enumerate
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()                 # I have to remember this shortcut (popping while storing the value)    
            maxArea = max(maxArea, height*(i - index))
            start = index                               # With this line you take into account the previous columns that sum for the total base of the new rectangle
        stack.append((start, h))                        # Here you storage the info form the previous comment
    for i, h in stack:
        maxArea = max(maxArea, h*(len(heights) - i))    # Here lie every rectangle that could be made from the beginning of the list
    return maxArea
            



heights = [2,1,5,6,2,3]
h2 = [2,1,2]
h3 = [5,4,1,2]

print(largestRectangleArea(h3))
