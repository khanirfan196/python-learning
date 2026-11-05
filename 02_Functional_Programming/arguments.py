# Arguments are the values passed to a called function.
# We can have a specific number of defined parameters at function.
# or we can have 'n' number of parameters.
# or we can have keyword and non-keyword paramters.

# A function with 3 parameters only.
def func1(a, b, c):
    print(a, b, c)

# A function with 3 parameters but 3rd parameter is optional. 
# and has default value. If not provided during call, it will take as None.
def func2(a, b, c=None):
    print(a, b, c)


# Function with 'n' no. of parameters, but no keywords.
def func3(*args):
    print(args)

# Function with 'n' no. of paramters but with keywords.
def func4(**kwargs):
    print(kwargs)


func1(1, 2, 3)

func2(1, 2)

func2(1, 2, 5)

func3(1, 2, 3, 4, 5, 6)

func4(name="irfan", age=35, city="chicago", state="il")



