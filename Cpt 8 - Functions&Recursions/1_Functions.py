def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)

'''
When we call a function with parentheses, the function gets execute and returns the result to the callable.
when we call a function without parentheses, a function reference is sent to the callable rather than executing the function itself.
for further reference - https://www.geeksforgeeks.org/python-invoking-functions-with-and-without-parentheses/

'''