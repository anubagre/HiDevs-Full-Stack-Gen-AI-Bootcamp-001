#Solution 2- Compact Address Book Management
import pickle
import re
from collections import Counter

class contactDetails:
    def __init__(self):
        try:
            with open("problem2_data_file.pickle","rb") as f:
                self.contact_details=pickle.load(f)
        except (FileNotFoundError, EOFError):
            self.contact_details = []

    def add_contact(self):
        for i in range(3):
            number= input("Enter contact number:")
            if len(number)!=10:
                print("Invalid Number")
                continue
            for entry in self.contact_details:
                if entry["number"] == number:
                    print("Number Already Exists.")
                    continue
            
            email= input("Enter email id:")
            if re.search("$@#.%",email)==False:
                print("Invalid email")

            for entry in self.contact_details:
                if entry["email"] == email:
                    print("Email Already Exists.")
                    continue

            name=input("Enter name in format-Firstname Lastname:") 
            try:
                Fname,LName=name.split()
            except:
                print("Invalid Input")
                continue

            s_details=input("Enter Details of StreetAddress, City(seperated by comma):")
            try:
                StreetAddress,City=s_details.split(",")
            except:
                print("Invalid Input")
                continue
            
            details=input("Enter Details of State, Country(seperated by comma):")
            try:
                State,Country=details.split(",")
                break
            except:
                print("Invalid Input")
                continue

        entry = {
            "Fname": Fname,
            "LName": LName,
            "StreetAddress": StreetAddress,
            "City": City,
            "State": State,
            "Country": Country,
            "Mobile": number,
            "email": email
        }
        self.contact_details.append(entry)
        with open("problem2_data_file.pickle","wb") as f:
            pickle.dump(self.contact_details, f)
    
    def count_occurrences(self, field):
        counter = Counter(entry[field] for entry in self.contact_details)
        for value, count in counter.most_common():
            print(f"{value}: {count}")

    def count_all_occurrences(self):
        print("Occurrences of First Names:")
        self.count_occurrences("Fname")
        print("\nOccurrences of Last Names:")
        self.count_occurrences("LName")
        print("\nOccurrences of Street Addresses:")
        self.count_occurrences("StreetAddress")


if __name__ == "__main__":
    contact_details = contactDetails()


    while True:
        title="\nCompact Address Book Management\n"
        print(title.center(20))
        choice = input("PRESS 1 to Add a person\nPRESS 2 to find number of occurrences of a Fname\nPRESS 3 to find number of occurrences of a Lname\nPRESS 4 to find the number of occurrences of a street\nPRESS 5 to count all occurences\nPRESS 6 to exit: ")
        if choice == "1":
            contact_details.add_contact()
        elif choice == "2":
            contact_details.count_occurrences("FName")
        elif choice == "3":
            contact_details.count_occurrences("LName")
        elif choice == "4":
            contact_details.count_occurrences("StreetAddress")
        elif choice == "5":
            contact_details.count_all_occurrences()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
