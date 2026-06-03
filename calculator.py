first = float(input("Enter first number "))
second = float(input("Enter second number "))
op = input("Enter symbol ")
if(op == "+"):
    print("The sum is ", first + second)
elif(op == "-"):
    print("The difference is ", first - second)
elif(op == "*"):
    print("The product is ", first * second)
elif(op == "/"):
    if(second != 0):
        print("The quotient is ", first / second)
    else:
        print("Cannot divide by zero")
else:
    print("Error. Not found" )
