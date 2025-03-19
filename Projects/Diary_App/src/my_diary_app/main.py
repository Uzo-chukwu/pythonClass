
from diaries import Diaries
import pickle


def save_diaries(diaries, filename="diaries.pkl"):

    try:
        with open(filename, "wb") as file:
            pickle.dump(diaries, file)
        print("Diaries saved successfully.")
    except Exception as e:
        print(f"Error saving diaries: {e}")

def load_diaries(filename="diaries.pkl"):

    try:
        with open(filename, "rb") as file:
            diaries = pickle.load(file)
        print("Diaries loaded successfully.")
        return diaries
    except FileNotFoundError:
        print("No saved diaries found. Starting with a new diary collection.")
        return Diaries()
    except Exception as e:
        print(f"Error loading diaries: {e}")
        return Diaries()

def display(message):
    print(message)



def landing_page(diaries):
    diaries = load_diaries()

    while True:
        choice = input("""
Welcome to MyDiaryApp!
Your secrets are safe with me 😊

1. Create new diary
2. Sign in
3. Exit
""")

        if choice == "1":
            create_new_diary(diaries)
        elif choice == "2":
            sign_in_and_use_diary(diaries)
        elif choice == "3":
            save_diaries(diaries)
            print("Goodbye!")
            break
        else:
            display("Invalid choice. Try again.")

def create_new_diary(diaries):
    username = input("Enter Your Username: ")
    password = input("Create Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match! Try again.")
        return

    try:
        diaries.create_diary(username, password)
        print("Diary created successfully!")
        main_menu(diaries.find_diary_by_username(username, password), diaries)
    except ValueError as e:
        print(f"Error creating diary: {e}")

def sign_in_and_use_diary(diaries):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        diary = diaries.find_diary_by_username(username, password)
        print(f"Login successful! Welcome back, {username}")
        main_menu(diary, diaries)
    except ValueError as e:
        print(e)

def main_menu(diary, diaries):
    while True:
        option = input("""
Main Menu:
1. Create an entry
2. Find entry by ID
3. Update an entry
4. Delete an entry
5. Lock diary
6. Delete diary
7. Exit (Back to sign-in)
""")

        if option == "1":
            create_entry(diary)
            save_diaries(diaries)  # Save after creating an entry
        elif option == "2":
            find_entry(diary)
        elif option == "3":
            update_entry(diary)
            save_diaries(diaries)  # Save after updating an entry
        elif option == "4":
            delete_entry(diary)
            save_diaries(diaries)  # Save after deleting an entry
        elif option == "5":
            lock_diary(diary)
        elif option == "6":
            delete_diary(diary, diaries)
        elif option == "7":
            save_diaries(diaries)  # Save before exiting
            print("Logging out... Redirecting to sign-in.")
            break
        else:
            print("Invalid choice. Try again.")

def create_entry(diary):
    if diary.get_is_locked():
        print("Diary is locked. Enter password to continue.")
        unlock_diary(diary)
        return

    title = input("Enter title: ")
    body = input("Enter entry body: ")

    try:
        diary.create_entry(title, body)
        print(f"Entry added successfully. Your id is {diary.get_entry_count() - 1}")
    except ValueError as e:
        print(f"Error creating entry: {e}")

def find_entry(diary):
    if diary.get_is_locked():
        print("Diary is locked. Enter password to continue.")
        unlock_diary(diary)
        return

    try:
        id = int(input("Enter entry ID: "))
        entry = diary.find_entry_by_id(id)
        print(f"Entry found:\n{entry}")
    except ValueError as e:
        print(e)

def update_entry(diary):
    if diary.get_is_locked():
        print("Diary is locked. Enter password to continue.")
        unlock_diary(diary)
        return

    try:
        id = int(input("Enter entry ID to update: "))
        new_title = input("Enter new title: ")
        new_body = input("Enter new body: ")
        diary.update_entry(id, new_title, new_body)
        print("Entry updated successfully.")
    except ValueError as e:
        print(e)

def delete_entry(diary):
    if diary.get_is_locked():
        print("Diary is locked. Enter password to continue.")
        unlock_diary(diary)
        return

    try:
        id = int(input("Enter entry ID to delete: "))
        confirm = input("Are you sure you want to delete this entry? (yes/no): ").lower()
        if confirm == "yes":
            diary.delete_entry(id)

            print("Entry deleted successfully.")
        else:
            print("Entry deletion canceled.")
    except ValueError as e:
        print(e)

def lock_diary(diary):
    diary.lock_diary()
    print("Diary locked.")

def unlock_diary(diary):
    password = input("Enter your password to unlock: ")
    if diary.validate_password(password):
        diary.unlock_diary()
        print("Diary unlocked.")
    else:
        print("Incorrect password. Diary remains locked.")

def delete_diary(diary, diaries):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm = input("Are you sure you want to delete your diary? (yes/no): ").lower()

    if confirm == "yes":
        try:
            diaries.remove_diary(username, password)
            display("Diary deleted successfully.")
            landing_page(diaries)
        except ValueError as e:
            print(e)
    else:
        print("Diary deletion canceled.")

if __name__ == "__main__":
    diaries = Diaries()
    landing_page(diaries)

