#Solution 1- Managing Personal Information with Python
import pickle
from datetime import datetime

class personalInfo:
    def __init__(self):
        try:
            with open("problem1_data_file.pickle", "rb") as f:
                self.personal_info, self.secret_names = pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.personal_info = {}
            self.secret_names = []

    def add_person(self):
        for i in range(3):
            name = input("Enter name: ")
            if name in self.personal_info or name in self.secret_names:
                print("Name already exists.")
                continue

            dob = input("Enter date of birth (YYYY-MM-DD): ")
            try:
                datetime.strptime(dob, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
                continue

            is_secret = input("Is the date of birth secret? (y/n) ")
            if is_secret.lower() == "y":
                self.secret_names.append(name)
            else:
                self.personal_info[name] = dob

            with open("problem1_data_file.pickle", "wb") as f:
                pickle.dump((self.personal_info, self.secret_names), f)

            print("Person added successfully.\n")
            return

        print("Maximum attempts reached. Exiting...\n")

    def get_dob(self, name):
        if name in self.personal_info:
            print(f"Date of birth for {name}: {self.personal_info[name]}\n")
        elif name in self.secret_names:
            print("secret\n")
        else:
            print("Name not found.\n")

if __name__ == "__main__":
    personal_info = personalInfo()

    while True:
        title="\nManaging Personal Information with Python\n"
        print(title.center(20))
        choice = input("PRESS 1 to Add a person\nPRESS 2 to get DOB\nPRESS 3 to exit: ")
        if choice == "1":
            personal_info.add_person()
        elif choice == "2":
            name = input("Enter name: ")
            personal_info.get_dob(name)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")