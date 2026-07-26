import json
import os
import hashlib


USER_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(USER_FILE):
        return {"users": []}

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(data):
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)


def register_user():
    users_data = load_users()

    print("\n========== CREATE ACCOUNT ==========")

    username = input("Enter username: ")

    for user in users_data["users"]:
        if user["username"] == username:
            print("❌ Username already exists.")
            return None

    password = input("Enter password: ")

    new_user = {
        "username": username,
        "password": hash_password(password)
    }

    users_data["users"].append(new_user)

    save_users(users_data)

    print("✅ Account created successfully!")

    return username


def login_user():
    users_data = load_users()

    print("\n========== LOGIN ==========")

    username = input("Username: ")
    password = input("Password: ")

    hashed_password = hash_password(password)

    for user in users_data["users"]:
        if user["username"] == username and user["password"] == hashed_password:
            print("✅ Login successful!")
            return username

    
    print("\n❌ Invalid username or password.")
    print("1. Try Again")
    print("2. Forgot Password")
    print("3. Back to Welcome Menu")

    choice = input("Enter your choice: ")
    if choice == "1":
       return login_user()

    elif choice == "2":
       forgot_password()
       return login_user()

    elif choice == "3":
       return None

    else:
       print("❌ Invalid choice.")
       return None

def forgot_password():
    users_data = load_users()

    print("\n========== FORGOT PASSWORD ==========")

    username = input("Enter Username: ")

    for user in users_data["users"]:

        if user["username"] == username:

            new_password = input("Enter New Password: ")
            confirm_password = input("Confirm New Password: ")

            if new_password != confirm_password:
                print("❌ Passwords do not match.")
                return

            user["password"] = hash_password(new_password)

            save_users(users_data)

            print("✅ Password reset successfully!")
            return

    print("❌ User not found.")

def change_password():
    users_data = load_users()

    username = input("Enter Username: ")

    for user in users_data["users"]:
        if user["username"] == username:

            current_password = input("Enter Current Password: ")

            if user["password"] != hash_password(current_password):
                print("❌ Incorrect current password.")
                return

            new_password = input("Enter New Password: ")
            confirm_password = input("Confirm New Password: ")

            if new_password != confirm_password:
                print("❌ Passwords do not match.")
                return

            user["password"] = hash_password(new_password)
            save_users(users_data)

            print("✅ Password changed successfully!")
            return

    print("❌ User not found.")