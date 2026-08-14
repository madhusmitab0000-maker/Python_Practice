# string
name= "Madhu" # a string always enclosed in quotes or double quotes
print(name) # prints the string value

#lenth of the string
print(len(name)) # prints the length of the string

# string slicing : used to extract a person of a sting
name = "Madhu"
print(name[0:3])
print(name[1:4:2])
print(name[2:])
print(name[:4])

# slicing string with negative index
name="Madhu"
print(name[-3:])
print(name[-5:-2])

# common string method: Lower and Upper

name="Madhu"
print(name.lower())
print(name.upper())

# Strip : Remove extra space
name=" Madhu  "
print(len(name))
name = name.strip()
print(name.strip())
print(len(name))

# Replace: raplace part of a string with another string
name=" Madhu  "
print(name.replace("Madhu","Jaanu"))

# Split:Split a string into a list based on a separator
name="madhu,ismail,sruti"
items=name.split(",")
print(items)

# Join:joins elemnets of a list a single string
name="madhu,ismail,sruti"
items=",".join(name)
print(items)

# Finds:finds the position of a substing
name="Hello Madhu"
position = name.find("Madhu")
print(position)

# startwith () and endswith(): checks whethar a strings starts or ends with a given value.
email="madhu@gmail.com"
print(email.startswith("madhu"))
print(email.endswith(".com"))

# String concartination:string can be combine using the + operator
first="hello"
second="Madhu"
print(first+ "" +second)

# String formating: 
# using f String
name = "Madhu"
age=21
message=f"My name is {name}and I am {age}year old"
print(message)

# Checking string content: python provide methods to checks string content
Data="python124"
print(Data.isalpha())
print(Data.isdigit())
print(Data.isalnum())

# String are Immumtable:String can not be changed
# data="python"
# data[0]="j"

# F string: 
name="Madhu"
age=21
print(f"My name is {name} and i an {age} year old")