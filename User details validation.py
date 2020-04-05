# User Data Validation
print("USER DATA VALIDATION")

from string import ascii_letters
import random

def show(detail):
    print("\nUser ", detail["User"])
    print("First name: ", detail["First_name"])
    print("Last name:  ", detail["Last_name"])
    print("Email:      ", detail["Email"])
    print("Password:   ", detail["Password"])

record = []
i = 0
i += 1
while i:
    print("\nFill in your details")
    user =  str(i)
    print("User ", i)
    i += 1

    fname = input("Enter your First name: ")
    lname = input("Enter your last name: ")
    email = input("Enter your Email: ")

    details = {"User":user, "First_name":fname, "Last_name":lname, "Email":email}

    ps = [fname[0], fname[1], lname[-2], lname[-1]]

    for b in range(5):
        ps.append(random.choice(ascii_letters))

    random.shuffle(ps)
    password = "".join(ps)

    print("\nPassword: ", password)

    option = input("Are you satisfied with this password? [y / n]: \n")
    if option == "n":
        while True:
            password1 = input("\nPassword should be equal or greater than 7 in lenght.\nEnter password of your choice: \n")
            if len(password1) < 7:
                print("Password should be equal or greater than 7 in lenght.\nInput another password: \n")
            else:
                details["Password"] = password1
                break
    else:
        details["Password"] = password

    print("Your details\n",details)
    record.append(details)
    print("Your details have been saved")

    again = input("\nDo you wish to continue? [y / n]: \n")
    if again == "y":
        print("")
    else:
    	print("End of user inputs.")
        break

print("\nRecord of users")
for a in range(len(record)):
    detail = record[a]
    show(detail)

