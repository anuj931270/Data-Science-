# Task: Validating Email Domain
user_email = input("Please enter your email address: ")
allowed_domain = "@gmail.com"
if user_email.lower().endswith(allowed_domain):
    print("Success: Your email is eligible for registration!")
else:
    print("Error: Registration failed. Only 'gmail.com' addresses are allowed.")