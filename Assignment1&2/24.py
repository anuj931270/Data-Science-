# Authentication System
user_name=input("Enter user name:")
if user_name == "anuj":
    password=input("Enter the pass:")
    if password== "anuj@6702":
        print("Authentication successful.")
    else:
        print("Authentication failed")
else:
    print("invalid user name")