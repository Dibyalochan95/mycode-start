marks = {}
maths = int(input("Enter maths marks "))
marks["maths"] = maths
physics = int(input("Enter physics marks "))
marks["physics"] = physics
chemistry = int(input("Enter chemistry marks "))
marks["chemistry"] = chemistry
biology = int(input("Enter biology marks "))
marks["biology"] = biology
english = int(input("Enter english marks "))
marks["english"] = english
marks["maximum marks"] = 500
total_marks = maths + physics + chemistry + biology + english
marks["total marks"] = total_marks
percentage = round((marks["total marks"] / marks["maximum marks"] * 100), 2)
marks["percentage"] = percentage
print("RESULTS")
print("Maths:", marks["maths"])
print("Physics:", marks["physics"])
print("Chemistry:", marks["chemistry"])
print("Biology:", marks["biology"])
print("English:", marks["english"])
print("Maximum Marks:", marks["maximum marks"])
print("Total Marks:", marks["total marks"])
print("Percentage:", percentage, "%")
if(percentage >= 90):
    print("Grade A+")
elif(percentage >= 80):
    print("Grade A")
elif(percentage >= 70):
    print("Grade B")
elif(percentage >= 60):
    print("Grade C")
elif(percentage >= 50):
    print("Grade D")
elif(percentage >= 40)    :
    print("Grade E")
else:
    print("Grade F")
if(percentage >= 75):    
    print("Congratulations! You qualify for JEE advanced")
else:
    print("Sorry! You do not qualify for JEE advanced")    
