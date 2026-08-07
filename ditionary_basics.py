student = {
    "name" : "Harry",
    "city" : "Delhi",
    "company" : "Meta"

}
print(student["city"])
# print(student["nameee"]) throw a error
print(student.get("nameee"))
student["city"] ="rairangpur"
print(student)

