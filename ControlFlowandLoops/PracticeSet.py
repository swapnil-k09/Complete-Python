# Python Conditionals & Loops - Practice Set
# Q1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
"""
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
"""

#  Q2. Create a program that checks if a person is eligible to vote (age >= 18).
"""
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
"""

# Q3. Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
# Q4. Ask the user to enter a day number (1–7) and print the corresponding day of the week using a match case statement.
"""
num = int(input("Enter a day number (1-7): "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
"""

#Q5. Write a program using match case that simulates a simple calculator.
"""
Oper = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

match Oper:
    case "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please use +, -, *, or /.")
"""

# Q6. Print numbers from 1 to 10 using a for loop.
"""
for i in range(1, 11):
    print(i)
"""

# Q7. Print the multiplication table of a number (entered by user).
"""
NUM = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{NUM} x {i} = {NUM * i}")
"""

#Q8. Calculate the sum of all numbers from 1 to 100 using a for loop.

"""
for i in range(1, 101):
    sum += i
print(f"The sum of all numbers from 1 to 100 is: {sum}")
"""
#Q9. Print the following pattern using a for loop:
"""
*
**
***
****
"""
#
'''
for i in range(1, 5):
    print(i*"*")
'''

#Q10. Print numbers from 1 to 10 using a while loop.
"""
num = 1
while num <= 10:
    print(num)
    num += 1
"""

#Q11. Write a program that keeps asking the user to enter a password until they enter the correct one.
"""
while password := input("Enter the password: ") != Pass:
    print("Incorrect password. Please try again.")
"""

# Q12. Use a while loop to reverse a given number (e.g., 123 → 321).
'''
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10 # It uses modulus operator to get the remainder when num is divided by 10, which gives the last digit.
    print(digit, end="")
    num //= 10
'''

#Q13. Use a for loop to print numbers from 1 to 10, but stop the loop if the number is 7 (use break).
"""
for i in range(1,11):
    if i ==7:
        break
    print(i)
"""

# Q14. Print numbers from 1 to 10, skipping the number 5 (use continue).
"""
for i in range(1,11):
    if i == 5:
        continue
    print(i)
"""
#Q15. Write a loop that goes through numbers 1 to 5, but does nothing for number 3 (use pass).
"""
for i in range(1,6):
    if i == 3:
        pass
    else:
        print(i)
"""
