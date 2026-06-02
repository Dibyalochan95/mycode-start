month = input("Enter month")
inc = float(input("Enter Income"))
ren = float(input("Enter Rent"))
gro = float(input("Enter Groceries expenses"))
elec = float(input("Enter electric bill"))
wat = float(input("Enter water bill"))
wifi = float(input("Enter Wifi bill"))
misc = float(input("Enter Miscellaneous Expenses"))
emi = float(input("Enter EMIs"))
tot = ren + gro +elec +wat + wifi + misc + emi
print("Total expenses for the month of ", month, "is Rs", tot )
exp = [ren, gro, elec, wat, wifi, misc, emi]
exp.sort()
print("The expenses are ", exp)
sav = inc - tot
print("Savings for the month of ", month, "is Rs", sav)
if(sav >= inc/2):
    print("Profit gained")
else:
    print("loss incurred")