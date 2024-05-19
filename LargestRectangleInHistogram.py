"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

def largestRectangleArea(heights):
    maxArea = 0
    stack = [0]
    for i in range(1, len(heights)):
        prevheight = stack[-1]
        while heights[i] < heights[prevheight]and stack:
            print(stack, i, maxArea)
            maxArea = max(maxArea, heights[prevheight]*(i - prevheight))
            stack.pop()
            if stack:
                prevheight = stack[-1]
        stack.append(i)
    print(stack)
    while len(stack) > 1:
        maxArea = max(maxArea, heights[prevheight]*(len(heights) - prevheight))
        stack.pop()
        prevheight = stack[-1]
    maxArea = max(maxArea, heights[prevheight]*(len(heights)))
    return maxArea
            



heights = [2,1,5,6,2,3]
h2 = [2,1,2]
h3 = [5,4,1,2]

print(largestRectangleArea(h3))
