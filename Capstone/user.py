import sqlite3
import bcrypt
import datetime

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

class User:

    def __init__(self):
        option = input("Would you like to login or create an account? Enter (L)ogin/(C)reate/(Q)uit: ").lower()
        if option == "c":
            return User.add_user(self)
        elif option == "l":
            return User.login(self)
        elif option == "q":
            return quit()
        else:
            option = input("Would you like to login or create an account? Enter (L)ogin/(C)reate/(Q)uit: Enter: ").lower()

    def add_user(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.email = input("Enter email: ")
        self.password = input("Enter password: ")
        hashed_password = User.hash_password(self, self.password)
        self.phone = input("Enter phone number: ")
        self.date_created = datetime.date.today()
        self.hire_date = datetime.date.today()
        self.user_type = 'user' 
        sql_statement = """
            INSERT INTO User (
                first_name, last_name, email, password, phone, date_created, hire_date, user_type
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?
            )
        """
        values = self.first_name, self.last_name, self.email, hashed_password, self.phone, self.date_created, self.hire_date, self.user_type
        return cursor.execute(sql_statement, values)
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_pwd

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        sql_statement = """
            SELECT user_id, email, password, user_type
            FROM User
            WHERE email = ?
        """
        emails = cursor.execute(sql_statement, (email,)).fetchone()
        if emails == None:
            return print("No email found")
        elif bcrypt.checkpw(password.encode('utf-8'), emails[2]):
            self.user_id = emails[1]
            self.user_type = emails[3]
            return print("Logged in successfully")
        else:
            return print("Email or password incorrect.")

    def show_actions(self):
        print("""
        1. View my competencies
        2. View my completed assessments
        3. Edit my information
        """)
        select = input("Select the number of the action you would like to take. (q to quit) Enter: ")
        if select == 1:
            return User.view_competencies()
        elif select == 2:
            return User.view_completed_assessments()
        elif select == 3:
            return User.edit_user_info()
        elif select == 'q':
            return exit()
        else:
            select = input("Select the number of the action you would like to take. Enter: ")
    
    def view_competencies(self):
        return

    def view_completed_assessments(self):
        return

    def edit_user_info(self, user_id):
        sql_statement = """
            SELECT first_name, last_name, email, password, phone FROM User
            WHERE user_id = ?
        """
        user_info = cursor.execute(sql_statement, (user_id,)).fetchone()
        print(user_info)
        print(f"\n1. First Name: {user_info[0]}")
        print(f"2. Last Name: {user_info[1]}")
        print(f"3. Email: {user_info[2]}")
        print(f"4. Password: *****\n")
        select = input("Select the number of the field you would like to change. Enter: ")
        
        return


    def take_assessment(self):
        return



class Manager(User):

    def __init__(self):
        self.date = datetime.date.today()
        return

    def add_manager(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.email = input("Enter email: ")
        self.password = input("Enter password: ")
        hashed_password = User.hash_password(self, self.password)
        self.phone = input("Enter phone number: ")
        date_created = self.date
        hire_date = self.date
        user_type = input("Enter user type (user/manager)").lower()
        #maybe do error handling right here. make sure user or manager is spelled correctly
        sql_statement = """
            INSERT INTO User (
                first_name, last_name, email, password, phone, date_created, hire_date, user_type
            )
            VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?
            )
        """
        values = self.first_name, self.last_name, self.email, hashed_password, self.phone, date_created, hire_date, user_type
        return cursor.execute(sql_statement, values)
    
    def create_compentency(self):
        name = input("Enter the name of the competency you'd like to create. Enter: ")
        date_created = self.date
        sql_statement = """
            INSERT INTO Competency (
                name, date_created
            )
            VALUES (
                ?, ?
            )
        """
        values = name, date_created
        return cursor.execute(sql_statement, values)

    def create_assessment(self, competency_id):
        name = input("Enter the name/description of the assessment. Enter: ")
        date_created = self.date
        sql_statement = """
            INSERT INTO Assessment (
                competency_id, name, date_created
            )
            VALUES (
                ?, ?, ?
            )
        """
        values = competency_id, name, date_created
        return cursor.execute(sql_statement, values)

cooper = User()
cooper.edit_user_info(1)

connection.commit()  