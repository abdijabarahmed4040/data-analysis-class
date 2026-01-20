#loops
database =[]

while True:
    #create
 name = input("Enter name:")
 schedule = input("Enter schedule:")
 payment = input("Enter payment:")
 subject = input("Enter subject:")
 phone = input("Enter your phone number:")



 student = {"name": name,
            "schedule": schedule,
            "payment":  payment,
            }
 
 database.append(student)
 print("if registration is done: y/n: ")

 if ask =="y/n":
  break
 print(database)

 for i in database:
  
  print(i)

#reading

print("\n\nShowing the registered students: ")
for index in range(len(database)):
 print(index+1,":-", database[index]["name"])



 print("nveiw and Editing: ")




choice = int*(input("Enter students number to veiw and edit detail"))

for index in range(len(database)):
 index_number =choice - 1
 if index == index_number:
  student = database[index_number]
  print("\nName:", student["name"])
  print("schedule:", student["schedule"])
  print("payment:", student["name"])

  editing = input("Editing - please enter a choice to edit:")
  if editing =="name":
   updated_name = input("Enter correct name: ")
   student["name"] = updated_name
   print("successfully updated the name!")
   print("\nName:", student["name"])
  print("schedule:", student["schedule"])
  print("payment:", student["name"])

elif editing == "schedule":
 student["schedule"] = updated_schedule
   print("successfully updated the schedule!")
   print("\nName:", student["name"])
   print("schedule:", student["schedule"])
   print("payment:", student["name"])

elif editing == "payment":
 student["payment"] = updated_payment
   print("successfully updated the payment!")
   print("\nName:", student["name"])
   print("schedule:", student["schedule"])
   print("payment:", student["name"])


   #delete


   print("deleting is started: ")

   student_deleteName = input("Enter the name of the student:")
   for student in database:
    if student_deleteName ==["name"]:
     database.remove(student)

     print("the student by the name of", student_deleteName,"is deleted successfully!!")









