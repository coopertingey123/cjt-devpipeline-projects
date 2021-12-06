import sqlite3
import bcrypt
import datetime

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()

class User:

    def __init__(self):
        self.date = datetime.date.today()
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
        cursor.execute(sql_statement, values)
        connection.commit()
        return
    
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
            print("No email found")
            try_again = input("Would you like to try again? Enter(y/n):").lower()
            if try_again == 'y':
                return User.login(self)
            else:
                return quit()
        elif bcrypt.checkpw(password.encode('utf-8'), emails[2]):
            self.user_id = emails[0]
            self.user_type = emails[3]
            if self.user_type == "manager":
                Manager.show_actions(self)
            return print("Logged in successfully")
        else:
            print("Email or password incorrect.")
            try_again = input("Would you like to try again? Enter(y/n):").lower()
            if try_again == 'y':
                return User.login(self)
            else: 
                return quit()

    def show_actions(self):
        print("""
        1. View my competencies
        2. View my completed assessments
        3. Edit my information
        """)
        print(self.user_id)
        select = input("Select the number of the action you would like to take. (q to quit) Enter: ")
        if select == "1":
            return User.view_competencies(self)
        elif select == "2":
            return User.view_completed_assessments(self)
        elif select == "3":
            return User.edit_user_info(self, self.user_id)
        elif select == 'q':
            return exit()
        else:
            select = input("Select the number of the action you would like to take. Enter: ")
    
    def view_competencies(self):
        sql_statement = """
            SELECT competency_id, name
            FROM Competency
        """
        competencies = cursor.execute(sql_statement).fetchall()
        print("Competency ID    Name/Description")
        for competency in competencies:
            print(f"{competency[0]:<16} {competency[1]}")
        return

    def view_assessments(self, competency_id):
        sql_statement = """
            SELECT assessment_id, name
            FROM Assessment
            WHERE competency_id = ?
        """
        assessments = cursor.execute(sql_statement, (competency_id,)).fetchall()
        print("Assessment ID    Name/Description")
        for assessment in assessments:
            print(f"{assessment[0]:<16} {assessment[1]}")
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
        if select == "1":
            new_value = input("Enter your new first name. Enter: ")
            edit_statement = """
                UPDATE User
                SET first_name = ?
                WHERE user_id = ?
            """
            values = new_value, user_id
            cursor.execute(edit_statement, values)
            print("\nFirst name successfully changed")
        elif select == "2":
            new_value = input("Enter your new last name. Enter: ")
            edit_statement = """
                UPDATE User
                SET last_name = ?
                WHERE user_id = ?
            """
            values = new_value, user_id
            cursor.execute(edit_statement, values)
            print("\nLast name successfully changed")
        elif select == "3":
            new_value = input("Enter your new email. Enter: ")
            edit_statement = """
                UPDATE User
                SET email = ?
                WHERE user_id = ?
            """
            values = new_value, user_id
            cursor.execute(edit_statement, values)
            print("\nField successfully changed")
        elif select == "4":
            old_pw = input("Enter your old password. Enter: ")
            sql_statement = """
                SELECT password
                FROM User
                WHERE user_id = ?
            """
            old_hashed_pw = cursor.execute(sql_statement, (user_id,)).fetchone()
            if bcrypt.checkpw(old_pw.encode('utf-8'), old_hashed_pw[0]):
                new_value = input("Enter your new password. Enter: ")
                new_hashed_pw = User.hash_password(self, new_value)
                edit_statement = """
                    UPDATE User
                    SET password = ?
                    WHERE user_id = ?
                """
                values = new_hashed_pw, user_id
                cursor.execute(edit_statement, values)
                print("\nField successfully changed")
            else:
                print("\nIncorrect password")
        connection.commit()  
        return


    def take_assessment(self):
        return



class Manager(User):

    # def __init__(self):
    #     self.date = datetime.date.today()
    #     return

    def show_actions(self):
        print("""
        As a manager, you can see, create, edit, and delete users, 
        competencies, assessments, and reports. Select the number of the
        section you want to access.""")
        print("""
        1. Users
        2. Competencies
        3. Reports
        """)
        select = input("Select the number of the section you would like to access. (q to quit) Enter: ")
        if select == "1":
            return User.view_competencies(self)
        elif select == "2":
            return User.view_completed_assessments(self)
        elif select == "3":
            return User.edit_user_info(self, self.user_id)
        elif select == 'q':
            return exit()
        else:
            select = input("Select the number of the action you would like to take. Enter: ")

    def view_user_actions(self):
        print("""
        1. Create User/Manager
        2. View all users
        3. Edit a user
        4. Search user by first/last name
        5. View specific users and their assessments
        6. View specific users and their competencies
        """)
        return

    def view_competency_actions(self):
        print("""
        1. Create a competency
        2. View competencies
        3. Edit competencies
        4. Create an assessment
        5. View assessments
        6. Edit assessments
        7. View specific users and their competencies
        8. View specific users and their assessments
        """)
        return

    def view_reports_actions(self):
        print("""
        Reports contain a summary of users and their competency levels for a given competency

        1. View All Users report 
        2. View Individual User report
        """)
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

    def view_users(self):
        sql_statement = """
            SELECT user_id, first_name, last_name, phone, email
            FROM User
        """
        users = cursor.execute(sql_statement).fetchall()
        print("User ID   First Name       Last Name        Phone        Email")
        for user in users:
            print(f"{user[0]:<9} {user[1]:<16} {user[2]:<16} {user[3]:<12} {user[4]}")
        return

    def search_user(self):
        search = input("Search User by first or last name. Search: ")
        sql_statement = """
            SELECT user_id, first_name, last_name, phone, email FROM User
            WHERE first_name LIKE "%?%"
            OR last_name LIKE "%?%"
        """
        values = search, search
        filtered_users = cursor.execute(sql_statement, values).fetchall()
        print("User ID   First Name       Last Name        Phone        Email")
        for user in filtered_users:
            print(f"{user[0]:<9} {user[1]:<16} {user[2]:<16} {user[3]:<12} {user[4]}")
        user_id = input("Select a user ID to take action on that user's account.")
        return self.select_action_after_user_select(self, user_id)

    def select_action_after_user_select(self, user_id):
        print("""
            1. Edit User
            2. View User Competencies
            3. View User Assessments
        """)
        action = input("Select action number. Enter: ")
        if action == "1":
            return User.edit_user_info(self, user_id)
        elif action == "2":
            return 
        elif action == "3":
            return
        return

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

    def give_user_a_competency(self, user_id):
        User.view_competencies(self)
        select_competency = input("Select a competency ID to view its assessments. Enter: ")
        User.view_assessments(self, select_competency)
        select_assessment = input("Select an assessment ID to give the user a score for the assessment. Enter: ")
        assessment_score = input("What did the user score on this assessment? Enter: ")
        sql_statement = """
            INSERT INTO Assessment_Results (
                assessment_id, user_id, score, date_taken, manager_id
            )
            VALUES (
                ?, ?, ?, ?, ?
            )
        """
        values = select_assessment, user_id, assessment_score, self.date, self.user_id
        return cursor.execute(sql_statement, values)
        #Here is where the data would go to the database.

        return

cooper = Manager()
# cooper.edit_user_info()
# cooper.view_competencies()
cooper.give_user_a_competency(1)

connection.commit()  