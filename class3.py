#input- output 
name = input("Enter name:")
schedule = input("Enter schedule:")
payment = input("Enter payment:")
subject = input("Enter subject:")
phone = input("Enter your phone number:")

#data structure - list and dictionary

student=[name, schedule, payment, subject, phone]

print("Hi", student[0])
print("your schedule is on",student [1])
print("which subject study", student[2])
print("i have sent you text massege phone number",[3])

location = input("Enter location:")

student.append(location)



student.insert(2, location)


#crud - create, read,  update, delete

print(student)
print("updating the name:")

correct_name =input("Enter correct name:")


student[0] = correct_name
print(student)

print(student)
print("updating the subject: ")

student.remove("Abdi")


student.remove("python")

print(student.remove)






























