def calculator ():
    print("simple calculator")
    print("select operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    choice = input("enter choice (1/2/3/4): ")
    num1 = float (input("enter first number : ")) 
    num2 = float(input ("enter second number : "))
    if choice == "1" :
        print("result :", num1+num2)
    elif choice == "2":
        print("result:", num1-num2)
    elif choice == "3":
        print("result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print ("result:", num1 / num2)
        else:
            print("error:division by zero")
    else:
        print("invalid input")
calculator ()

