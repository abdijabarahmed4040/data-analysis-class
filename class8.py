#conditions
age = 20
if age >= 18:
    print("You are an adult")

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")


logged_in = False
if not logged_in:
    print("Please login")



password = input("Enter password: ")
if password == "admin123":
    print("Login successful")
else:
    print("Wrong password")









