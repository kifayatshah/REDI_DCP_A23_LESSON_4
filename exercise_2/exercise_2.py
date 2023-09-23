new_dict = {"name": "xyz", "age": 0}
print("Previous :", new_dict)

# 1. Write a python code to accept name and age from the user and update in the dictionary
# Result: After Update: {'name': 'sameer', 'age': 15}

# Write your code here
name = input("What is your name? Name: ")
age = int(input("What is your age? Age: "))
new_dict.update({"name": name, "age": age})

print("After Update:", new_dict)
