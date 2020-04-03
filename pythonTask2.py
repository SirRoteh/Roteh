answer = (input("New User? Yes/NO: ")).upper()
allUserDetails = []
while answer == "YES":
    first_name = (input("Enter your First Name: ")).capitalize()
    last_name = (input("Enter your Last Name: ")).capitalize()
    email = input("Enter your email address: ")

    random = "4xaZB"
    password = first_name[0] + first_name[1] + last_name[-2] + last_name[-1] + random
    print(f"Your password is {password}: ")
    response = (input(f"Do you like the password {password}?  Yes/No ")).upper()

    if response == "YES":
        print(f'''Your Login Details are:
                First Name: {first_name}
                Last Name: {last_name}
                Email Address: {email}
                Password: {password}
    ''')
    elif response == "NO":
        password = input("Create a password: ")
        while len(password) < 7:
            print("Password must be more than 7 characters.")
            password = input("Create another password: ")
        else:
            print(f'''Your Login Details are:
                    First Name: {first_name}
                    Last Name: {last_name}
                    Email Address: {email}
                    Password: {password}
        ''')
    answer = (input("New User? Yes/NO: ")).upper()

    userDetails = [first_name, last_name, email, password]
    allUserDetails.append(userDetails)
else:
    print("Total User's Info Collected: ")
    print(len(allUserDetails))
    print("FIRST-NAME LAST-NAME EMAIL PASSWORD ")
    for info in allUserDetails:
        print(info)
