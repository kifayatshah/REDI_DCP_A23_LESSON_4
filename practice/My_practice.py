from functools import reduce
import random

# Lambda Example 1
x = lambda a: a+1

# Equivalent function
def increment(a):
    return a+1

print(x(5))

# Lambda Example 2
y = lambda b, c:  b+c
print(y(5, 8))

# Equivalent function
def sum_int(b, c):
    return b+c

# List comprehension from string to list
abc_string = "a,b,c"
abc_list = [x for x in abc_string.split(",")]
print(abc_list)

# List comprehension extended
names = ["Noah", "Emma", "Oliver", "Charlotte", "Elijah", "Amelia", "James" ,"Ava"]
a_names = [name for name in names if name.startswith("A")]
print(a_names)

# Dict comprehension Example: Get numbers from A-H
contacts = {"Noah": "166 5968014",
    "Emma": "167 4668754",
    "Oliver": "155 6178788",
    "Charlotte": "178 8047640",
    "Elijah": "166 7160871",
    "Amelia": "170 8099931",
    "James": "159 9219533",
    "Ava": "145 7395303"}

a_h_names = {name: number for name, number in contacts.items() if name[0] < "H"}

for key, value in a_h_names.items():
    print("Name: " + key + "\nNumber: " + value)
    print()

# Map Example 1
number_lst = [1, 2, 3, 4, 5]

def square(n):
    return n*n

map_object = map(square, number_lst)

print(list(map_object))

# Filter Example 1

def is_healthy(food):
   healthy_food = ["Apple", "Apricot", "Araza", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant"]
   return True if food in healthy_food else False
   
snack = ["Apple", "Coca Cola", "Avocado", "Chips"]

print(is_healthy("Banana"))

healthy_sanck = filter(is_healthy, snack)

print(list(healthy_sanck))

# Reduce Example 1
shopping_expenses = [34.5, 25.0, 57.78, 82.9, 2.89]

print(reduce(lambda a,b: a+b, shopping_expenses))


# Reduce Example 2
name = ["A", "n", "n", "a"]

print(reduce(lambda a,b: a+b, name))


# Homework
donors_raw = ["Michael 187",
    "Christopher 135",
    "Jessica 100",
    "Matthew 169",
    "Ashley 188",
    "Jennifer 157",
    "Joshua 175",
    "Amanda 181",
    "Daniel 171",
    "David 104",
    "James 147",
    "Robert 172",
    "John 161",
    "Joseph 151",
    "Andrew 111",
    "Ryan 134",
    "Brandon 148",
    "Jason 172",
    "Justin 163",
    "Sarah 137",
    "John 173",
    "Joseph 169",
    "Andrew 162",
    "Ryan 189",
    "Brandon 126",
    "Jason 138",
    "Ryan 135",
    "Brandon 186",
    "Jason 186",
    "Justin 179",
    "Sarah 172",
    "William 153",
    "Jonathan 145",
    "Stephanie 157",
    "Brian 197"]

"""
- donors_raw contains a list with the name of donors of an organization and the donated amount in EUR

- Create a dictionary from the list. Take into consideration that the same person can donate several times! The key of the list should be the name of the person and the value the total donated amount

"""

donors_dict = {}
for donor in donors_raw:
    name = donor.split(" ")[0]
    amount = int(donor.split(" ")[1])
    
    if name in donors_dict:
        donors_dict.update({name: amount + donors_dict.get(name)})
    else:
        donors_dict.update({name: amount})

"""
- Create a list of all the amount using list comprehension
- You can iterate over a dictionary using dict.items()
"""

donations = [y for x, y in donors_dict.items()]


"""
- Altruism Inc. is a big sponsor of this charity. They promised to contribute the same amount of money than the people
- Use map to apply the function double_donation() to the whole list
"""
def double_donation(x):
    return x*2

donations = list(map(double_donation, donations))



"""
- Get the sum of the list of donations
- Use reduce() and a lambda
"""

total_donations = reduce(lambda a,b: a+b, donations)


"""
- Filter the dictionary to have only big donors. This are people which donated more than 300 EUR
- Use dictionary comprehension
"""

big_donors = {key: value for key, value in donors_dict.items() if value > 300}
