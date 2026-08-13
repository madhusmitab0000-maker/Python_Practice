numbers = (1, 2, 3)
names = ("Alice", "Bob", "Charlie")
mixed = (1, "Python", 3.5, True)

# A tuple with one element must include a trailing comma
single = (5,)
print(type(single))

single = (5)
print(type(single))

# Tuple element are accessed usig indexs
items = ("apple", "banana", "orange")
print(items[0])
print(items[2])

# Accessing Tuple Elements
# Tuple elements are accessed using indexes.
items = ("apple", "banana", "orange")
print(items[0])
print(items[2])


# Negative Indexing
# Negative indexes start from the end of the tuple.
items = ("apple", "banana", "orange")
print(items[-1])
print(items[-2])

# Tuple Length
# Use the 
# len() function to get the number of elements in a tuple.
items = ("apple", "banana", "orange")
count = len(items)

# Tuple Slicing
# Slicing is used to extract part of a tuple.
items = ("apple", "banana", "orange", "mango")
print(items[1:3])
print(items[:2])
print(items[2:])

# Tuples are Immutable
# # Tuples cannot be modified after creation.
# items = ("apple", "banana", "orange")
# items[1] = "grapes"
# This will cause error

# Tuple Methods
# Tuples have fewer built in methods compared to lists.
items = ("apple", "banana", "apple")
count = items.count("apple")
print(count)
# index()
# Returns the index of the first occurrence of a value.
items = ("apple", "banana", "orange")
position = items.index("banana")
print(position)

# Looping Through a Tuple
# You can loop through tuple elements using a 
items = ("apple", "banana", "orange")
for item in items:
 print(item)

#  Tuple Packing and Unpacking
# Packing
# Multiple values can be packed into a tuple.
data = 10, 20, 30
print(data)

# Unpacking
# Tuple values can be unpacked into separate variables.
a, b, c = data
print(a)
print(b)

# Converting Between List and Tuple
# You can convert a tuple to a list and vice versa.

items = ("apple", "banana")
items_list = list(items)
items_tuple = tuple(items_list)
print(type(items_list))
print(type(items_tuple))

