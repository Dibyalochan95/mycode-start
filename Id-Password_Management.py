db= {
    "admin1" : "admin1pwd",
    "jaykant@95" : "JP@120596",
    "Vivek@80085" : "VA@290695",
    "Rak@3456" : "RakAg@1997",
    "Rohini124" : "RohAg@2002",
    "Ali@3457" : "AliM@2001",
    "Peter@2004" : "Pete#1992"


}
Names = {
    db["admin1"] : "Mahesh Babu",
    db["jaykant@95"] : "Jaykant Patel",
    db["Vivek@80085"] : "Vivek Sharma",
    db["Rak@3456"] : "Rakshit Agarwal",
    db["Rohini124"] : "Rohini Agarwal",
    db["Ali@3457"] : "Ali Mirza",
    db["Peter@2004"] : "Peter Johnson"
}
user_id = input("Enter your ID: ")
password = input("Enter your password: ")
if user_id in db and db[user_id] == password:
    print("Login successful!")
    print("Welcome,", Names[password]) 
else:
    print("Invalid ID or password. Please try again.")
   