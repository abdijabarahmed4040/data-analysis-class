#function
def calculator():
    print("this is start of the calculator: ")
    num1 = float(input("Enter num1!: "))
    opr = input("Enter operator:")
    num2 = float(input("Enter num2:"))
#return
if opr =="+":
    print("sum", num1 + num2)

elif opr == "*":
    print("mul:", num1 * num2)

elif opr == "-":
    print("subs:", num1 - num2)
elif opr == "/":
    print("divide:", num1 / num2) 


if opr =="+":
    return("sum:", num1 + num2)

elif opr == "*":
    return("mul:", num1 * num2)

elif opr == "-":
    return("subs:", num1 - num2)
elif opr == "/":
    return("divide:", num1 / num2) 


else:

    print("invalid operator!")