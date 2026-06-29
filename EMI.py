principal = float(input("Enter principal amount "))
rate = float(input("Enter rate of interest "))
time = int(input("Enter time "))
if principal < 0 or rate < 0 or time < 0:
    print("Please enter valid input")
else:
    si = (principal*rate*time)/100
amount = principal + si
emi = amount/time  
for mon in range(1, time + 1):
    print("the emi for month", mon, "is", emi)
print("Total interest payable is ", si)
print("The total amount payable is ", amount)

    