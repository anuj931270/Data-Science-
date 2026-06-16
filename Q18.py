# Task : Authentication System.
VALID_USERNAME = "user1"
VALID_PASSWORD = "pass@123"
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")
if entered_username == VALID_USERNAME and entered_password == VALID_PASSWORD:
    print("Authentication successful.")
else:
    print("Authentication failed.")