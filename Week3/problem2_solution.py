#Solution 2- Compact Address Book Management
import pickle
import re

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

            if number in self.contact_details:
                print("Number Already Exists.")
                continue
            
            email= input("Enter email id:")
            if re.search("$@#.%",email)==False:
                print("Invalid email")

            if email in self.contact_details:
                print("Email Already Exists.")
                continue
            '''details=input("Enter following values seperated by comma(,)-(Fname, LName, StreetAddress, City, State, Country):")
            try:
                Fname, LName, StreetAddress, City, State, Country=details.split(",")
            except:
                print("Invalid Input")
                continue'''
        info={}
        info[number]={email}#,Fname, LName, StreetAddress, City, State, Country}
        self.contact_details.append(info)
        with open("problem2_data_file.pickle","wb") as f:
        pickle.dump(self.contact_details, f)
   
        print("Maximum attempts reached. Exiting...\n")

if __name__ == "__main__":
    contact_details = contactDetails()


    while True:
        title="\nCompact Address Book Management\n"
        print(title.center(20))
        choice = input("PRESS 1 to Add a person\nPRESS 2 to find number of occurrences of a Fname\nPRESS 3 to find number of occurrences \
                       of a Lname\nPRESS 4 to find the number of occurrences of a street\nPRESS 5 to exit: ")
        if choice == "1":
            contact_details.add_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

