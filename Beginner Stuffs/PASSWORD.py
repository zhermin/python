# LOGIN SYSTEM

print ("Welcome to Python!")
print ("")
print ("Please enter your desired username below.")
print ("Note: Your username has to be at least 5 digits long")

username = input ()
while len(username) < 5:
    print ("Please enter a username of at least 5 digits")
    username = input ()

print ("")    
print ("Hi, " + username + ", and welcome to Python.")
print ("")

print ("Please enter an alphanumerical password below.")
print ("Note: Your password has to be at least 7 digits long")

password = input ()
while len(password) < 7 or password.isalnum() == False:
    print ("Please enter a password of at least 7 digits")
    password = input ()
print ("Your password has been accepted")
print ("")
print ("Please re-enter your password for confirmation")

repassword = input ()
while repassword != password:
    print ("Please re-enter your password")
    repassword = input()
print ("Thank you for creating an account, " + username + ".")
