#Function 1- Registration

def register_user():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip().lower()

    try:
        age = int(input("Enter your age: "))

        if name == "":
            print("Name cannot be empty")

        elif "@" not in email:
            print("Invalid Email")

        else:
            with open("main_users.txt", "a") as file:
                file.write(name + " - " + str(age) + " - " + email + "\n")
            print("Registration Successful ✅")



    except:
        print("Invalid age")

#function 2:
def view_users():
    try:
        with open("main_users.txt", "r") as file:
            data = file.read()
            print("\n--- Registered Users ---")
            print(data)

    except:
        print("No users found or file does not exist")

#fuction 3:
while True:
    print("\n--- User Management System ---")
    print("1. Register User")
    print("2. View Users")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        view_users()
    
    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid option")

