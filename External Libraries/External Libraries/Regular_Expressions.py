# Regular Expressions in Python
# Regular expressions (regex) are powerful tools for pattern matching in strings. Python's re module provides support for regex.

# import re
 
# text = "The quick brown fox jumps over the lazy dog."
# # Search for a pattern
# match = re.search("brown", text)
# if match:
#     print("Match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())
 
# # Find all occurrences of a pattern
# matches = re.findall("the", text, re.IGNORECASE)  # Case-insensitive search
# print("Matches:", matches)
 
# # Replace all occurrences of a pattern
# new_text = re.sub("fox", "cat", text)
# print("New text:", new_text)
 
# # Compile a regex for efficiency (if used multiple times)
# pattern = re.compile(r"\b\w+\b")  # Matches whole words
# words = pattern.findall(text)
# print("Words:", words)

# Lets understand the regex pattern re.compile(r"\b\w+\b") used in the above code:

# Part	Meaning
# \b	Word boundary (ensures we match full words, not parts of words)
# \w+	One or more word characters (letters, digits, underscores)
# \b	Word boundary (ensures we match entire words)



