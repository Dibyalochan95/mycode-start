principal = float(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = int(input("Enter time in years: "))
n = int(input("Enter no times principal compounded: "))
amount = principal*(1 + rate/(100*n))**(n*time)
if principal <= 0 or rate <= 0 or time <= 0 or n <= 0:
    print("*"*30)
    print("Invalid input. Please try again ")
    print("*"*30)
else:
    print("*"*30)
    print("Amount payable :", round(amount,2))
    print("*"*30)
    print("Interest payable is ", round(amount-principal, 2))
    print("*"*30)

breakdown = input("Enter yes or no :")
if breakdown == "yes":
    for month in range(1,time*12 +1):
        amount = principal*(1 + rate/(100*12))**(month)
        print("Month :", month, ":", round(amount))
elif breakdown == "no":
    print("Have a nice day")
else:
    print("wrong input")    
        
    