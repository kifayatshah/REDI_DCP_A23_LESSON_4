# 1. Use list comprehension to create the following lists:
# Create a list of all integers from 1 to 100 that are divisible by 7. Hint: use the modulo (%) operator in the if clause.
# Result: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

solution = [x for x in range(1, 101) if x % 7 == 0]
print(solution)
