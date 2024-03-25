#!/usr/bin/env python3
import csv

class User:
    def __init__(self, id, name, first_name, gender, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth):
        """
        Initializes a User object with additional parental information.
        """
        self.id = id
        self.name = name
        self.first_name = first_name
        self.gender = gender
        self.address = address
        self.nationality = nationality
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.father_name = father_name
        self.father_first_name = father_first_name
        self.father_date_of_birth = father_date_of_birth
        self.mother_name = mother_name
        self.mother_first_name = mother_first_name
        self.mother_date_of_birth = mother_date_of_birth
        self.children = []


    def verify_parents(self, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth):
        """
        Verifies parents' information in the database.
        """
        if (self.father_name == father_name and self.father_first_name == father_first_name and self.father_date_of_birth == father_date_of_birth) \
           and (self.mother_name == mother_name and self.mother_first_name == mother_first_name and self.mother_date_of_birth == mother_date_of_birth):
            return True
        else:
            return False


    def add_child(self, child):
        """
        Adds a child to the user's record.
        """
        if self.verify_parents(father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth) == True:
            self.children.append(child)
            print("Child added successfully!")
        else:
            print("Failed to add child: Parents not verified.")

    #def add_parent(self, parent):
        """"
        Adds a parent to the user's record'
        """
    #self.parent.append(parent)
    #print("Child added successfully!")   

    def remove_child(self, child):
        """
        Removes a child from the user's record.
        """
        if child in self.children:
            self.children.remove(child)
        else:
            print("Child not found.")

    def remove_parent(self, parent):
        """
        Removes a parent from the user's record.
        """
        if (self.father_name == parent.name and self.father_first_name == parent.first_name and self.father_date_of_birth == parent.date_of_birth) or \
           (self.mother_name == parent.name and self.mother_first_name == parent.first_name and self.mother_date_of_birth == parent.date_of_birth):
            self.father_name = ""
            self.father_first_name = ""
            self.father_date_of_birth = ""
            self.mother_name = ""
            self.mother_first_name = ""
            self.mother_date_of_birth = ""
            print("Parent removed successfully.")
        else:
            print("Parent not found.")
    
    def remove_self(self, platform):
        """
        Removes the user from the platform's user list and from the global family tree.
        """
        # Remove the user from the platform's user list
        platform.users.remove(self)



class FamilyTree:
    def __init__(self):
        """
        Initializes a FamilyTree object to manage a collection of Person objects.
        """
        self.people = []

    def add_person(self, person):
        """
        Adds a person to the family tree.
        """
        self.people.append(person)

    def remove_person(self, person):
        """
        Removes a person from the family tree.
        """
        self.people.remove(person)



class Platform:
    def __init__(self):
        """
        Initializes a Platform object to manage user registration and family trees.
        """
        self.users = []
        self.global_tree = FamilyTree()

    def register_user(self, id, name, first_name, gender, address, nationality, phone, date_of_birth,
                      father_name, father_first_name, father_date_of_birth,
                      mother_name, mother_first_name, mother_date_of_birth):
        """
        Registers a user in the platform and adds them to the global family tree.
        """
        # Create a new user instance
        user = User(id, name, first_name, gender, address, nationality, phone, date_of_birth,
                    father_name, father_first_name, father_date_of_birth,
                    mother_name, mother_first_name, mother_date_of_birth)
        
        # Add the user to the global family tree
        self.global_tree.add_person(user)
        

        # Add the user to the platform's user list
        self.users.append(user)

        return user



class Administrator:
    def __init__(self, name, first_name, address, nationality, phone, date_of_birth):
        """
        Initializes an Administrator object.
        """
        self.name = name
        self.first_name = first_name
        self.address = address
        self.nationality = nationality
        self.phone = phone
        self.date_of_birth = date_of_birth

    def remove_node(self, person):
        """
        Removes a node and its descendants from the family tree.
        """
        pass

    def track_tree_size(self, family_tree):
        """
        Tracks the evolution of the family tree's size.
        """
        pass

    def find_most_represented_family(self, family_tree):
        """
        Finds the most represented family in the global tree.
        """
        pass

    def other_functionalities(self):
        """
        Other functionalities to be defined.
        """
        pass


class BDD:
    
    def NewPersonInCSV(id, name, first_name, gender, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth):
        
        with open('ArbreGen.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            data = [id, name, first_name, gender, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth]
            writer.writerow(data)

    def DelPersonInCSV(id):
        
        with open('ArbreGen.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
    
        with open('ArbreGen.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            for row in rows:
                if row[0] != id:
                    writer.writerow(row)


    def DelSearchCSV(name, first_name, birth_date):
        
        with open('ArbreGen.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            
            for row in reader:
                
                if row['nom'] == name and row['prénom'] == first_name and row['naissance'] == birth_date:
                    id = row['id']
                    BDD.DelPersonInCSV(id)
                    print("Father removed successfully!")
        
        return None
    

    def SearchIdInCSV(self):
        last_id = None
        with open ('ArbreGen.csv', 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            
            for row in reader :
                last_id=int(row[0])
            
            if last_id is not None :
                return last_id + 1
            
            else :
                return 1
    


#____________________________________   INTERFACE ____________________________


welcome_message = """
Welcome to our Family Tree Platform!

We're thrilled to have you join our community dedicated to creating and managing family trees. With our platform, you can easily trace your ancestry, connect with relatives, and explore your family history.

Whether you're just getting started or you're a seasoned genealogist, our platform offers a wide range of features to help you build and explore your family tree with ease.

Feel free to explore the various functionalities, add your family members, and embark on a journey of discovery through your family's rich heritage.

Happy exploring!


Pauline, Alize and François Platform   


"""
print(welcome_message)


# Create an instance of the platform
platform = Platform()



# Register a new user
print("Please enter your information below:")
id = BDD.SearchIdInCSV()
print(id)
name = input("Last Name: ")
first_name = input("First Name: ")
gender = input("Gender: ")
address = input("Address: ")
nationality = input("Nationality: ")
phone = input("Phone Number: ")
date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
father_name = input("Father's Last Name: ")
father_first_name = input("Father's First Name: ")
father_date_of_birth = input("Father's Date of Birth (YYYY-MM-DD): ")
mother_name = input("Mother's Last Name: ")
mother_first_name = input("Mother's First Name: ")
mother_date_of_birth = input("Mother's Date of Birth (YYYY-MM-DD): ")

# Register the user with the entered information
new_user = platform.register_user(id, name, first_name, gender, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth)
BDD.NewPersonInCSV(id, name, first_name, gender, address, nationality, phone, date_of_birth, father_name, father_first_name, father_date_of_birth, mother_name, mother_first_name, mother_date_of_birth)

# Sample data for 10 users
users_data = [
    ("12", "Dupont", "Jean", "M", "123 Rue de la République", "France", "01-23-45-67-89", "1980-05-15",
     "Dupont", "Pierre", "1950-02-10", "Durand", "Marie", "1955-08-20"),
    ("11", "Dubois", "Marie", "F", "456 Avenue Victor Hugo", "France", "02-34-56-78-90", "1975-07-20",
     "Dubois", "Jacques", "1955-11-25", "Martin", "Isabelle", "1960-04-15"),
    ("10", "Moreau", "François", "M", "789 Boulevard Saint-Germain", "France", "03-45-67-89-01", "1990-09-10",
     "Moreau", "Philippe", "1965-06-30", "Lefebvre", "Catherine", "1970-12-05"),
    ("9", "Lefevre", "Sophie", "F", "234 Rue du Faubourg", "France", "04-56-78-90-12", "1982-03-25",
     "Lefevre", "Michel", "1958-09-15", "Garcia", "Nathalie", "1963-11-20"),
    ("8", "Roux", "Antoine", "M", "567 Rue de la Paix", "France", "05-67-89-01-23", "1995-11-05",
     "Roux", "Bernard", "1970-04-20", "Blanc", "Sylvie", "1975-08-10"),
    ("7", "Girard", "Elodie", "F", "890 Boulevard des Capucines", "France", "06-78-90-12-34", "1988-12-30",
     "Girard", "David", "1960-11-12", "Robin", "Christine", "1965-02-25"),
    ("6", "Bonnet", "Julien", "M", "123 Rue de Rivoli", "France", "07-90-12-34-56", "1984-06-18",
     "Bonnet", "Vincent", "1963-07-22", "Chevalier", "Sophie", "1968-10-15"),
    ("5", "Thomas", "Cécile", "F", "456 Avenue de la Grande Armée", "France", "08-01-23-45-67", "1992-10-08",
     "Thomas", "Alain", "1975-01-05", "Rousseau", "Sandrine", "1980-03-30"),
    ("4", "Robert", "Lucas", "M", "789 Rue de la Madeleine", "France", "09-34-56-78-90", "1987-04-02",
     "Robert", "Franck", "1967-12-12", "Petit", "Caroline", "1972-09-25"),
    ("3", "Richard", "Manon", "F", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Richard", "Olivier", "1980-05-18", "Leroy", "Elise", "1985-11-15"),
    ("2", "Trepos", "Stephane", "M", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Trepos", "Bertand", "1980-05-18", "Leroy", "Elise", "1985-11-15"),
    ("1", "Poulichet", "Patricia", "F", "234 Avenue des Champs-Élysées", "France", "10-45-67-89-01", "1998-08-20",
     "Poulichet", "Joseph", "1980-05-18", "Poulichet", "Irène", "1985-11-15"),
]


# Register 10 users
for data in users_data:
    platform.register_user(*data)

for data in users_data:
    BDD.NewPersonInCSV(*data)


# Display potential parents
print("Potential Parents for", new_user.first_name, new_user.name, ":")



for user in platform.users:
    if (user.name == new_user.father_name and user.first_name == new_user.father_first_name and user.date_of_birth == new_user.father_date_of_birth) or \
       (user.name == new_user.mother_name and user.first_name == new_user.mother_first_name and user.date_of_birth == new_user.mother_date_of_birth):
        print("    ", user.first_name, user.name, user.date_of_birth)


# After registering, prompt the user to choose an action
print(" ")
print("You are now registered. What would you like to do? ")
print(" ")
print("1. Add a direct parent")
print("2. Add a direct child")
print("3. Remove a person ")

choice = input("Enter the number corresponding to your choice: ")

if choice == "1":
    # Prompt the user to enter parent information
    parent_name = input("Enter the parent's last name: ")
    parent_first_name = input("Enter the parent's first name: ")
    parent_date_of_birth = input("Enter the parent's date of birth (YYYY-MM-DD): ")
    parent_gender = input("Enter the parent's gender (M/F): ")
    parent_id = BDD.SearchIdInCSV()
    # Create the parent user
    parent_user = platform.register_user("",parent_name, parent_first_name, parent_gender, "", "", "", parent_date_of_birth, "", "", "", "", "", "")

    BDD.NewPersonInCSV(parent_id, parent_name, parent_first_name, parent_gender, "", "", "", parent_date_of_birth, "", "", "", "", "", "")

    # Add the parent to the user's record
    new_user.add_parent(parent_user)
    print("Parent added successfully!")
    
elif choice == "2":
    # Prompt the user to enter child information
    child_name = input("Enter the child's last name: ")
    child_first_name = input("Enter the child's first name: ")
    child_date_of_birth = input("Enter the child's date of birth (YYYY-MM-DD): ")
    child_gender = input("Enter the child's gender (M/F): ")
    child_id = BDD.SearchIdInCSV() 
    # Create the child user
    child_user = platform.register_user("", child_name, child_first_name, child_gender, "", "", "", child_date_of_birth, "", "", "", "", "", "")

    BDD.NewPersonInCSV(child_id,child_name, child_first_name, child_gender, "", "", "", child_date_of_birth, "", "", "", "", "", "")
    # Add the child to the user's record

    new_user.add_child(child_user)
    print("Child added successfully!")

elif choice == "3":
    
    print(" ")
    print("Which node do you want to remove? ")
    print(" ")
    print("1. Yourself ")
    print("2. A child ")    
    print("3. Father ")
    print("4. Mother ")
    remove_choice = input("Enter the number corresponding to your choice: ")

if remove_choice == "1":
    
    BDD.DelSearchCSV(new_user.name, new_user.first_name, new_user.date_of_birth)
    print("User removed successfully!")
        
elif remove_choice == "2":

    child_name = input("Enter the child's last name: ")
    child_first_name = input("Enter the child's first name: ")
    child_date_of_birth = input("Enter the child's date of birth (YYYY-MM-DD): ")


    for child in new_user.children:
        
        BDD.DelSearchCSV(child_name, child_first_name, child_date_of_birth)
        print("Child removed successfully")

        break

    else:
        print("Child not found.")
   
elif remove_choice == "3":

    parent_name_P = input("Enter the parent's name")
    parent_first_name_P = input("Enter the parent's first_name")
    parent_date_of_birth_P = input("Enter the parent's birth date")

    for user in platform.users:

        BDD.DelSearchCSV(parent_name_P, parent_first_name_P, parent_date_of_birth_P)

        break

elif remove_choice == "4":

    parent_name_M = input("Enter the parent's name")
    parent_first_name_M = input("Enter the parent's first_name")
    parent_date_of_birth_M = input("Enter the parent's birth date")

    for user in platform.users:
        
        BDD.DelSearchCSV(parent_name_M, parent_first_name_M, parent_date_of_birth_M)
        print("Mother removed successfully!")
        
        break
    else:
        print("Mother not found.")

else:
    print("Invalid choice.")


"""
# Example Usage:
# Creating an instance of an administrator
admin = Administrator("Trepos", "Pauline", "1 avenue champs elysée 75001 Paris", "Française", "0612233445", "17/02/2003")

# Creating an instance of a family tree
family_tree = FamilyTree()

# Creating an instance of a user
user = User("Moutarde", "Ketchup", "Mcdo de Cergy", "Américain", "+600020305", "01/01/1970",
            "Gog", "Hot", "01/01/1850", "Nini", "Pa", "02/01/1850")

# Authenticating the user
#Authentication.authenticate_user(user)

# Adding the user to the family tree
family_tree.add_person(user)
"""



