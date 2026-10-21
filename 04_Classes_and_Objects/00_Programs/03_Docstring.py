def hello():
    """
    This is a docstring. Its a string which is written inside a function before defining any thing.
    """

print(hello())

# prints the string inside a function. 
print(hello.__doc__)

# we can print with help() also.
help(hello)


'''
About Docstrings:

There are types of docstrings we can define in a function.
1) Single Quotes
2) Double Quotes
3) Google Styled
4) Numpy Style
5) Single Line
6) For Classes.

A docstring's first line should contain the highlevel or summary information of
that function or class. Then an empty line.

In the following line, we can describe about the function or its related members.
Just keep leaving lines wherever required. 

The other ways are also similar just that you use numbering for stating points. 
For classes, explain about classes and its related functions, arguments etc. 
'''