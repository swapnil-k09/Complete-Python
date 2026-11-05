# 1. File I/O Basics
# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.
# Open notes.txt, read its content, and print it to the console.
"""#Writing into a new file
f = open("notes.txt", "a")
String = """
# Learning Python is fun!
"""
f.write(String)
f.close()

# Reading a file
f = open("notes.txt", "r")
a = f.read()
print(a)
f.close()
"""

# 2. Read, Write, and Append Files
# Write a program that writes three lines of text to a file tasks.txt.
# Open tasks.txt in append mode and add a new line "Task Completed!".
# Read the file and print all lines as a list using readlines().

"""# Writing a File
f = open("Tasks.txt", "w")
String = """
# Fill Water.
# List Groceries.
# Mop Floor.
"""
f.write(String)
f.close()

#Apending
f = open("Tasks.txt", "a")
String = "Task Completed!"
f.write(String)
f.close()

# Read File
r = open("Tasks.txt", "r")
d = r.read()
print(d)
f.close()

"""


# 3. OS and Shutil Modules
# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder
# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)         
"""import os
import shutil
current_dir = os.getcwd()
print(current_dir)
list = os.listdir(".")
print(list)
# new_folder = os.mkdir("my_folder")
list2 = os.listdir(".")
print(list2)
shutil.copy("notes.txt", "notes2.txt")
shutil.move("my_file.txt", "new_directory/")
os.remove("file.txt")
"""
# 4. Creating Command Line Utilities
# Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

# python count_lines.py tasks.txt
# # Output: Number of lines: 4
# Write a command-line utility search_word.py that takes two arguments:
# A filename
# A word to search and prints how many times the word appears in the file.

"""import sys
filename = sys.argv[1]
with open(filename, "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))"""

"""import sys
filename = sys.argv[1]
word = sys.argv[2]
with open(filename, "r") as file:
    data = file.read()
count = data.split().count(word)
print(f"'{word}' appears {count} times.")
"""

# 5. Bonus Challenges
# Write a program that reads a file and creates another file with all words converted to uppercase.
# Create a script that deletes all .tmp files from the current directory using os and os.remove().
# Write a Python command-line tool that takes a folder name and prints the total size of all files inside it (use os.path.getsize()).

"""with open("input.txt", "r") as file:
    data = file.read()
data = data.upper()
with open("output.txt", "w") as file:
    file.write(data)
print("File converted to uppercase successfully!")"""


"""import os
for file in os.listdir():
    if file.endswith(".tmp"):
        os.remove(file)
        print(f"Deleted: {file}")
print("Cleanup completed!")
"""

"""import os
import sys
folder = sys.argv[1]
total_size = 0
for file in os.listdir(folder):
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        total_size += os.path.getsize(path)
print(f"Total size: {total_size} bytes")"""