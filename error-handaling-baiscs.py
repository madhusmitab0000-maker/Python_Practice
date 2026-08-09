print("Initializing....")

a = int(input("Enter a: \n"))
b = int(input("Enter b: \n"))
try:
    print("The valur of a/b is : ", a/b)
except Exception as e:
 
    print("some error occure, ", e)

print("Thank you....")
