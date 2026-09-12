# # Functions
# # Functions help in reusability and modularity in Python.

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  # Output: Hello, Alice!


# Key Points:
# Defined using def keyword.
# Function name should be meaningful.
# Use return to send a value back.

# Eg,
def average(a,b,c):
    d = ((a+b+c)/3)
    print(d)
    # or
    # print((a+b+c)/3)
average(1,2,3)      #Call Function average
# or
def avg(*args):                     #Effective as yo can take multiple values (*args). avg(args) takes only one value but * can be used where you want multiple values.
    return sum(args) / len(args)
    # or
    # print(sum(args) / len(args))
avg(1, 2, 3)        #Call Function avg