# Here we are reading a json file into a python dictonary. Reading and writing files will be covered in another lesson.
import json

with open("exercise_3/data.json", "r") as file:
    file_content = file.read()
    quotes = json.loads(file_content)

# The variable qoutes is a dictornary containing all the information.
# Have a look in the data.json file to see the key value pairs or print the dictonary
# 1. Print all quotes with auther.
#
# Result:
# The chief task in life is simply this: to identify and separate matters so that I can say clearly to myself which are externals not under my control, and which have to do with the choices I actually control. Where then do I look for good and evil? Not to uncontrollable externals, but within myself to the choices that are my own ...
# by Epictetus
#
# ...
# Add a empty line in between quotes
#

# Write your code here
'''for quote in quotes["quotes"]:
    x=quote["author"]
    y= quote["quote"]
    print(f"{y}\n", f"by {x}\n")
'''