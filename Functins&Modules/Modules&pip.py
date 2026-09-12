# # Importing Modules
# # Python provides built-in and third-party modules.

# # Example: Using the math module
# import math
# print(math.sqrt(16))  # Output: 4.0

# # # Creating Your Own Module
# # Save this as mymodule.py:
# def greet(name):
#     return f"Hello, {name}!"

# # Import in another file:
# import mymodule
# print(mymodule.greet("Alice"))  # Output: Hello, Alice!

# # Installing External Libraries with pip
# # pip install requests

# # Example usage:
# import requests
# response = requests.get("https://api.github.com")
# print(response.status_code)

# import requests
# req = requests.get("https://www.google.com")
# print(req.text)
