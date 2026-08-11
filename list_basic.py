names = ["ismail", "madhu" , "Harry", "Larry"]
elementns = [1,34, 67, False , True]

print(names)

print(type(names))
print(elementns)
print(type(elementns))
# print(elementns[0])
# print(elementns[1])
# print(names[0])
print(elementns[1:4])

# Lists in python are mutable
elementns[2]= 69
print(elementns)