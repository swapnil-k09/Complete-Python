# Creating Command Line Utilities
# You can use Python to create simple command-line utilities. The argparse module makes it easier to handle command-line arguments.

"""import argparse
 
parser = argparse.ArgumentParser(description="A simple command-line utility.")
parser.add_argument("filename", help="The file to process.")
parser.add_argument("-n", "--number", type=int, default=1, help="Number of times to repeat the output.")
 
args = parser.parse_args()
 
try:
    with open(args.filename, "r") as file:
        content = file.read()
        for _ in range(args.number):
            print(content)
except FileNotFoundError:
    print("File not found.")"""
 

# To run this script from the command line:

# python my_script.py my_file.txt -n 3

# This will print the contents of my_file.txt three times. You can learn more about argparse in the Python documentation.



"""import argparse
parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument("num1", type=float, help="First Number")
parser.add_argument("num2", type=float, help="Second Number")
parser.add_argument("operation",choices=["add","sub","mul","div"],help="Operation")
args = parser.parse_args()
print(args)
if(args.operation=="add"):
    print({args.num1 + args.num2})
elif(args.operation=="sub"):
    print({args.num1 - args.num2})
elif(args.operation=="mul"):
    print({args.num1 * args.num2})
elif(args.operation=="div"):
    print({args.num1 / args.num2})
else:
    print("Error Occured!")
# if __name__ == "__main__":
#     main()
"""
