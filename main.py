import json
import os
FILE = "passwords.json"
# Create file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)
def save_password(site, username, password):
    with open(FILE, "r") as f:
        data = json.load(f)
    data[site] = {"username": username, "password": password}
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Password saved successfully!")
def get_password(site):
    with open(FILE, "r") as f:
        data = json.load(f)
    if site in data:
        print(f"Site: {site}")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {data[site]['password']}")
    else:
        print("No password found for this site.")
def menu():
    while True:
        print("\nPassword Manager")
        print("1. Save Password")
        print("2. Get Password")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            save_password(site, username, password)
        elif choice == "2":
            site = input("Enter site name: ")
            get_password(site)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
menu()