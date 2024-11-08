print("Making the first project of full stack web development\n")
print("Simple Calculator making using python\n")

print("1: Addition ")
print("2: Subtraction ")
print("3: Multiplacation ")
print("4: Divition")
print("5: Power\n")

option = int(input("Sellect an operation for perform : "))

if 0<option<6:
    num1 = int(input("Enter your first number : "))
    num2 = int(input("Enter your second number : "))

    if option == 1:
        sum = num1 + num2
        print("Addition is = " , (sum))
    elif option == 2:
        sub = num1-num2
        print("Subtraction is = " , (sub))
    elif option == 3:
        mul = num1*num2
        print("Multiplecation is = " , (mul))
    elif option == 4:
        div = num1/num2
        print("Divition is = " , (div))
    elif option == 5:
        power = pow(num1,num2)
        print(f"Result of {num1} = " , power)

    else:
        print("Invalid Input")

else:
    print(" Invalid input \n Perform an Operation between 1 to 5")


