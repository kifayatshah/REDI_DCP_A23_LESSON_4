set_1 = {"A", "B", "E", "J", "L", "O", "K", "Y", "N"}
set_2 = {"c", "B", "D", "N", "P", "Y", "A", "J", "M"}

# 1. Print the common elements in both sets
# Result: {'Y', 'A', 'N', 'J', 'B'}
print(set_1.intersection(set_2))


# 2. Print total number of unique elements from both sets
# Result: 13
print(len(set_1.union(set_2)))

# 3. Print alphabets that are in set2 but not in set1
# Result: {'c', 'P', 'D', 'M'}
print(set_2.difference(set_1))
