# Walrus operator
# Introduction
# The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name "walrus operator" comes from the operator's resemblance to the eyes and tusks of a walrus.

# Use Cases
# Conditional Expressions: The most common use case is within if statements, while loops, and list comprehensions, where you need to both test a condition and use the value that was tested.

# Without walrus operator
"""data = input("Enter a value (or 'quit' to exit): ")
while data != "quit":
    print(f"You entered: {data}")
    data = input("Enter a value (or 'quit' to exit): ")
 
# With walrus operator
while (data := input("Enter a value (or 'quit' to exit): ")) != "quit":
    print(f"You entered: {data}")"""

# In the "with walrus" example, the input is assigned to data and compared to "quit" in a single expression.

# List Comprehensions: You can avoid repeated calculations or function calls within a list comprehension.

"""numbers = [1, 2, 3, 4, 5]
 
# Without walrus operator:  calculate x * 2 twice
results = [x * 2 for x in numbers if x * 2 > 5]
 
# With walrus operator: calculate x * 2 only once
results = [y for x in numbers if (y := x * 2) > 5]

Reading Files: You can read lines from a file and process them within a loop.

# Without Walrus
with open("my_file.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
 
# With Walrus
with open("my_file.txt", "r") as f:
    while (line := f.readline()):
        print(line.strip())"""

# Considerations
# Readability: While the walrus operator can make code more concise, it can also make it harder to read if overused. Use it judiciously where it improves clarity.
# Scope: The variable assigned using := is scoped to the surrounding block (e.g., the if statement, while loop, or list comprehension).
# Precedence: The walrus operator has lower precedence than most other operators. Parentheses are often needed to ensure the expression is evaluated as intended.


"""while(data:=input("Enter a Number: ")):
    print(f"You entered: {data}")
    if data == "quit": break
"""