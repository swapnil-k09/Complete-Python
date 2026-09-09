# Taking User Input in Python

# In Python, you can take user input using the input() function. The input() function reads a line from the input (usually from the user), converts it into a string, and returns it.
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")  # This will greet the user with their name.
# you can also convert the input to other data types if needed, for example, using int() to convert to an integer or float() to convert to a floating-point number.
#eg,
age = int(input("Enter your age: "))  # Convert the input to an integer
print("You are " + str(age) + " years old.")  # Convert the integer back to a string for printing