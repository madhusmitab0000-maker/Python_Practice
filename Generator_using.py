def complex_calculation(i):
    #some complex calculation here
    return i*i
def get_numbers():
    for i in range(5):
        yield complex_calculation(i)
a= get_numbers()
# print(a,type(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
