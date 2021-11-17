import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

class User:
    def __init__(self, user_id, first_name, last_name, city, state, email, password, date_created, age, gender):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.email = email
        self.password = password
        self.date_created = date_created
        self.age = age
        self.gender = gender

    def change_password(self):
        updated_password = input("Enter new password: ")
        sql_1 = "UPDATE Users SET password = ? WHERE user_id = ?"
        values = updated_password, str(self.user_id)
        cursor.execute(sql_1, values)
        return

    def update_email(self):
        updated_email = input("Enter new email: ")
        sql_1 = "UPDATE Users SET email = ? WHERE user_id = ?"
        values = updated_email, str(self.user_id)
        cursor.execute(sql_1, values)
        return 

    def show_details(self):
        return print(
            f"""
            User: {self.user_id}
            First: {self.first_name}
            Last: {self.last_name}
            City: {self.city}
            State: {self.state}
            Email: {self.email}
            Password: {self.password}
            Date Created: {self.date_created}
            Age: {self.age}
            Gender: {self.gender}
            """
        )

    def create_user(self):
        create_user = """
        INSERT INTO Users (
            user_id, first_name, last_name, city, state, email, password, date_created, age, gender
        )
        VALUES (
            ?,?,?,?,?,?,?,?,?,?
        )
        """
        list_of_values = self.user_id, self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.age, self.gender
        return cursor.execute(create_user, list_of_values)
    
    def load_user(self):
        sql_1 = "SELECT * FROM Users WHERE user_id = ?"
        user_id = str(self.user_id)
        rows = cursor.execute(sql_1, user_id).fetchone()
        return print(rows)

class Organization(User):
    def __init__(self, org_id, name, city, state):
        self.org_id = org_id
        self.name = name
        self.city = city
        self.state = state

    def show_organization(self):
        return print(
            f"""
            Name: {self.name}
            City: {self.city}
            State: {self.state}
            """
        )
    
    def add_org(self):
        create_org = """
            INSERT INTO Organizations (
                org_id, name, city, state
            )
            VALUES (
                ?,?,?,?
            )
            """
        list_of_values = self.org_id, self.name, self.city, self.state
        return cursor.execute(create_org, list_of_values)

    
    def add_user(self):
        jimmy = User(2, "Jimmy", "John", "Cleveland", "OH", "jimmy@jimmy.com", "123", "1/23/2014", 30, "male", 2)
        jimmy.create_user()

    
        



cooper = User(1, "Cooper", "Tingey", "Provo", "UT", "coopergmail.com", "123", "11/13/2021", 23, "male")

cooper_company = Organization(2, "Cooper's cooler company", "Provo", "Utah")

cooper_company.add_org()
# cooper.show_details()
# cooper.create_user()
# cooper.load_user()
# cooper.update_email()
# cooper.change_password()
# cooper.check_pw_match()




connection.commit()  
