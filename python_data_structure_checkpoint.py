#Question 1: Multiply all items in a list

sample_list = [2, 3, 6]
result = 1
for item in sample_list:
    result *= item
print("Result =", result)


 #Question 2: Sort list of tuples by last element

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(sample_list, key=lambda x: x[-1])
print("Sorted list:", sorted_list)


#Question 3: Combine two dictionaries and add values for common keys

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
result = {}

# Combine and add values for common keys
for key in set(d1) | set(d2):
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined dictionary:", result)


 #Question 4: Generate dictionary of squares from 1 to n

n = 8
squares = {i: i * i for i in range(1, n + 1)}
print("Squares dictionary:", squares)


#Question 5: Sort tuple by float value

items = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_items = sorted(items, key=lambda x: float(x[1]), reverse=True)
print("Sorted items:", sorted_items)


#Question 6: Create, iterate, add and remove from a set

# Create a set
my_set = {0, 1, 2, 3, 4}
print("Initial Set:", my_set)

# Iterate over the set
print("Iterating over set:")
for item in my_set:
    print(item)

# Add members to the set
my_set.add(5)
my_set.update([6, 7])
print("Set after adding items:", my_set)

# Remove items from the set
my_set.remove(3)  # Removes 3
my_set.discard(10)  # No error if 10 not in set
print("Set after removal:", my_set)