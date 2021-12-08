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
        return self.show_actions()
    
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
            print("\nLogged in successfully")
            return self.show_actions()
        else:
            print("Email or password incorrect.")
            try_again = input("Would you like to try again? Enter(y/n):").lower()
            if try_again == 'y':
                return User.login(self)
            else: 
                return quit()

    def show_actions(self):
        print("""
        1. View competencies
        2. View my assessments & scores
        3. Edit my information
        """)
        select = input("Select the number of the action you would like to take. (q to quit) Enter: ")
        if select == "1":
            User.view_competencies(self)
            return self.reroute()
        elif select == "2":
            return self.view_my_assessments()
        elif select == "3":
            return self.edit_user_info(self.user_id)
        elif select == 'q':
            return exit()
        else:
            self.show_actions()
    
    def view_competencies(self):
        sql_statement = """
            SELECT competency_id, name
            FROM Competency
        """
        competencies = cursor.execute(sql_statement).fetchall()
        print("\nCompetency ID    Name/Description")
        for competency in competencies:
            print(f"{competency[0]:<16} {competency[1]}")
        return

    def view_assessments(self):
        sql_statement = """
            SELECT assessment_id, c.name, a.name
            FROM Assessment a, Competency c
            JOIN Competency
            ON a.competency_id = c.competency_id
        """
        assessments = cursor.execute(sql_statement).fetchall()
        print("\nAssessment ID  Competency          Name/Description")
        for assessment in assessments:
            print(f"{assessment[0]:<15}{assessment[1]:<20}{assessment[2]}")
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
            print("\nEmail successfully changed")
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
                print("\nPassword successfully changed")
            else:
                print("\nIncorrect password")
        connection.commit()  
        return self.reroute()

    def view_my_assessments(self):
        sql_statement = """
        SELECT ar.user_id, (u.first_name || " " || u.last_name), a.name, ar.score
        FROM Assessment_Results ar
        JOIN User u 
        ON  ar.user_id = u.user_id
        JOIN Assessment a
        ON a.assessment_id = ar.assessment_id
        WHERE u.user_id = ?
        """
        assessments = cursor.execute(sql_statement, (self.user_id,)).fetchall()
        print("User ID   User Name            Assessment Name                Score")
        for assessment in assessments:
            print(f"{assessment[0]:<9} {assessment[1]:<20} {assessment[2]:<30} {assessment[3]}")
        return self.reroute()

    def reroute(self):
        option = input("Would you like to take another action or quit? (a for action, q to quit). Enter: ")
        if option == "a":
            return self.show_actions()
        elif option == "q":
            return quit()
        else:
            self.reroute()



class Manager(User):

    def reroute(self):
        option = input("Would you like to take another action or quit? (a for action, q to quit). Enter: ")
        if option == "a":
            return self.show_actions()
        elif option == "q":
            return quit()
        else:
            self.reroute()

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
            return self.view_user_actions()
        elif select == "2":
            return self.view_competency_actions()
        elif select == "3":
            return self.view_reports_actions(self.user_id)
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
        """)
        select = input("Select the number of the action you would like to take (q to quit). Enter: ")
        if select == "1":
            return self.add_manager()
        elif select == "2":
            return self.view_users()
        elif select == "3":
            return User.edit_user_info()
        elif select == "4":
            return self.search_user()
        elif select == "q":
            return exit()
        else:
            self.view_user_actions()

    def view_competency_actions(self):
        print("""
        1. Create a competency
        2. View competencies
        3. Edit competencies
        4. Create an assessment
        5. View assessments
        6. Edit assessments
        7. Select a User to view competencies
        """)
        select = input("Select the number of the action you would like to take (q to quit). Enter: ")
        if select == "1":
            return self.create_compentency()
        elif select == "2":
            return self.view_competencies()
        elif select == "3":
            return self.edit_competency()
        elif select == "4":
            return self.create_assessment()
        elif select == "5":
            return User.view_assessments()
        elif select == "6":
            return self.edit_assessment()
        elif select == "7":
            return self.view_users()
        elif select == "q":
            return exit()
        else:
            return self.view_competency_actions()

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
        user_type = input("Enter user type (user/manager). Enter: ").lower()
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
        cursor.execute(sql_statement, values)
        connection.commit()
        print("\nManager account created successfully.")
        return self.reroute()

    def view_users(self):
        sql_statement = """
            SELECT user_id, first_name, last_name, phone, email
            FROM User
        """
        users = cursor.execute(sql_statement).fetchall()
        print("\nUser ID   First Name       Last Name        Phone        Email")
        for user in users:
            print(f"{user[0]:<9} {user[1]:<16} {user[2]:<16} {user[3]:<12} {user[4]}")
        return self.select_action_for_user()

    def search_user(self):
        search = input("Search User by first or last name. Search: ")
        sql_statement = """
            SELECT user_id, first_name, last_name, phone, email FROM User
            WHERE first_name LIKE "%?%"
            OR last_name LIKE "%?%"
        """
        values = search, search
        filtered_users = cursor.execute(sql_statement, values).fetchall()
        print("\nUser ID   First Name       Last Name        Phone        Email")
        for user in filtered_users:
            print(f"{user[0]:<9} {user[1]:<16} {user[2]:<16} {user[3]:<12} {user[4]}")
        return self.select_action_for_user()

    def select_action_for_user(self):
        user_id = input("Select the user ID of the user you want to take action on. Enter: ")
        print("""
            1. Edit User
            2. View User Assessments and Competencies
            3. Give a User a score on an assessment
            4. Back to main menu
        """)
        action = input("Select action number (q to quit). Enter: ")
        if action == "1":
            return User.edit_user_info(self, user_id)
        elif action == "2":
            #This one should link me to the user and the score for his/her assessments
            return self.view_all_user_assessments()
        elif action == "3":
            #This should link me to the function that gives a user a score
            self.give_user_a_competency()
            return
        elif action == "4":
            return self.show_actions()
        elif action == "q":
            return quit()
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
        cursor.execute(sql_statement, values)
        connection.commit()
        print("\nCompetency created successfully.")
        return self.reroute()

    def edit_competency(self):
        User.view_competencies(self)
        select = input("Select the ID of the competency you would like to edit. Enter: ")
        new_name = input("Enter the new name of the compency you'd like to edit. Enter: ")
        sql_statement = """
            UPDATE Competency
            SET name = ?
            WHERE competency_id = ?
        """
        values = new_name, select
        cursor.execute(sql_statement, values) 
        connection.commit()
        print("\nCompetency has been updated.")
        return self.reroute()

    def create_assessment(self):
        User.view_competencies(self)
        select_competency = input("\nSelect the id of the competency the assessment will be listed under. Enter: ")
        name = input("\nEnter the name/description of the assessment. Enter: ")
        date_created = self.date
        sql_statement = """
            INSERT INTO Assessment (
                competency_id, name, date_created
            )
            VALUES (
                ?, ?, ?
            )
        """
        values = select_competency, name, date_created
        cursor.execute(sql_statement, values)
        connection.commit()
        print("\nAssessment created successfully.")
        return self.reroute()

    def edit_assessment(self):
        User.view_assessments(self)
        select_assessment = input("Select the assessment ID to edit. Enter: ")
        new_name = input("Enter the new name of the assessment you'd like to edit. Enter: ")
        sql_statement = """
            UPDATE Assessment
            SET name = ?
            WHERE assessment_id = ?
        """
        values = new_name, select_assessment
        cursor.execute(sql_statement, values) 
        connection.commit()
        print("\nAssessment has been updated.")
        return self.reroute()

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
        cursor.execute(sql_statement, values)
        connection.commit()
        print("\nUser score for this competency has been updated.")
        return self.reroute()

    def view_all_user_assessments(self):
        sql_statement = """
        SELECT ar.user_id, (u.first_name || " " || u.last_name), a.name, ar.score
        FROM Assessment_Results ar
        JOIN User u 
        ON  ar.user_id = u.user_id
        JOIN Assessment a
        ON a.assessment_id = ar.assessment_id
        """
        assessments = cursor.execute(sql_statement, (self.user_id,)).fetchall()
        print("User ID   User Name            Assessment Name                Score")
        for assessment in assessments:
            print(f"{assessment[0]:<9} {assessment[1]:<20} {assessment[2]:<30} {assessment[3]}")
        return self.reroute()


cooper = Manager()

connection.commit()  