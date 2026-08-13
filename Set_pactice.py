# Sets in Python

# Creating a Set
# Sets are created using curly braces {} or the set ()function
numbers = {1, 2, 3, 4}
names = {"Alice", "Bob", "Charlie"}
print(numbers)
print(names)

# To create an empty set, use set() .
empty_set = set()
print(empty_set)

# Unique Elements in a Set
# Sets automatically remove duplicate values.
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

# Accessing Set Elements
# Sets do not support indexing or slicing because they are unordered.
# To access elements, you must loop through the set.
items = {"apple", "banana", "orange"}
for item in items:
 print(item)

#  Adding Elements to a Set
# add()
# Adds a single element to the set.
items = {"apple", "banana"}
items.add("orange")
print(items)

# update()
# Adds multiple elements from another iterable.
items = {"apple", "banana"}
items.update(["orange", "mango"])
print(items)

# Removing Elements from a Set
# remove()
# Removes a specified element. Raises an error if the element does not exist.
items = {"apple", "banana"}
items.remove("banana")
print(items)


# discard()
# Removes a specified element without raising an error.
items = {"apple", "banana"}
items.discard("grapes")
print(items)


# pop()
# Removes and returns a random element.
items = {"apple", "banana", "orange"}
items.pop()
print(items)


# clear()
# Removes all elements from the set.
items = {"apple", "banana"}
items.clear()
print(items)

# Set Operations
# Sets support mathematical set operations.

# Union
# Combines elements from both sets.
a = {1, 2, 3}
b = {3, 4, 5}
result = a.union(b)
print(result)

# Intersection
# Returns common elements between sets.
result = a.intersection(b)
print(result)


# Difference
# Returns elements present in the first set but not in the second.
result = a.difference(b)
print(result)

# Symmetric Difference
# Returns elements present in either set but not in both.
result = a.symmetric_difference(b)
print(result)

# Symmetric Difference
# Returns elements present in either set but not in both.
result = a.symmetric_difference(b)
print(result)

# Sets are Mutable
# Sets can be modified after creation.
items = {"apple", "banana"}
items.add("orange")
print(items)
