# f=open("qwe.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f = open("JohnDoe.txt", "w")
# String = """
# Hes a nice guy
# I know him since a year
# """
# f.write(String)
# f.close()

f = open("JohnDoe.txt", "a")
String = """
He lives initially in Pheonix, Arizona, United States of America.
"""
f.write(String)
f.close()