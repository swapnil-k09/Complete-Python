# Break, COntinue, Pass statements are used to control the flow of loops in Python.
# - The break statement is used to exit a loop prematurely when a certain condition is met.
# Syntax of break statement:
"""
for item in sequence:
    if condition:
        break  # Exit the loop if the condition is met
    # Code to execute for each item
"""

# Eg. of break statement in a loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)  # Print the value of i for all other cases


# - The continue statement is used to skip the current iteration of a loop and move on to the next iteration.
# Syntax of continue statement:
"""
for item in sequence:
    if condition:
        continue  # Skip the rest of the code in this iteration and move to the next iteration
    # Code to execute for each item
"""

# Eg. of continue statement in a loop
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the code when i is 2
    print(i)  # Print the value of i for all other cases


# - The pass statement is a null operation; it is used as a placeholder in loops or functions where code is syntactically required but you do not want to execute any code.
# Syntax of pass statement:
"""
for item in sequence:
    if condition:
        pass  # Do nothing and continue with the next iteration
    # Code to execute for each item
"""

# Eg. of pass statement in a loop
for i in range(5):
    if i == 2:
        pass  # Do nothing when i is 2
    else:
        print(i)  # Print the value of i for all other cases