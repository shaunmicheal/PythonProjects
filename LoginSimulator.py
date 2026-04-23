credentials = { 
    "user_name" : "miltah",
    "password" : "mil123"
    }

def login ():
    print("WELCOME TO THE LOGIN SIMULATOR")
   
    user_name = input("Enter your name: ")
    password = input("Enter your password:  ")

    if user_name == credentials["user_name"] and password == credentials["password"]:
        print(f"Acess granted! Welcome, {user_name}.")
    else:

        print(f"Acess denied! The name or password entered is incorrect. Try again: ")

login()
