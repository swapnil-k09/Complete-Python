# Match Case Statements in Python
"""Match case statements are a new feature introduced in Python 3.10.
They allow you to match values against patterns and execute code based on the matched pattern.
It simplifies complex conditional logic."""
# Syntax of match case statement:
"""
match value:
    case pattern1:
        # Code to execute if value matches pattern1
    case pattern2:
        # Code to execute if value matches pattern2
    case _:
        # Default case (if no patterns match)
"""
# Eg,
"""
tatus = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")
"""
