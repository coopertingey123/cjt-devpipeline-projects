import sqlite3

connection = sqlite3.connect('dp_customers.db')
cursor = connection.cursor()

class User:
    def __init__(self, first_name, last_name, city, state, email, password, age, gender):
        self.user_id = None
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.email = email
        self.password = password
        self.date_created = "2021-11-21 09:00"
        self.age = age
        self.gender = gender

    def change_password(self, updated_password):
        self.password = updated_password
        return

    def update_email(self, updated_email):
        self.email = updated_email
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

    def create_user_in_db(self):
        create_user = """
            INSERT INTO Users (
                first_name, last_name, city, state, email, password, date_created, age, gender
            )
            VALUES (
                ?,?,?,?,?,?,?,?,?
            );
        """
        list_of_values = self.first_name, self.last_name, self.city, self.state, self.email, self.password, self.date_created, self.age, self.gender
        return cursor.execute(create_user, list_of_values)

    def save_user(self):
        user_id = cursor.execute("SELECT user_id FROM Users WHERE email = ?", (self.email,)).fetchone()
        save_user = """
            UPDATE Users
            SET 
                email = ?,
                password = ?
            WHERE
                user_id = ?
            ;
        """
        values = self.email, self.password, user_id[0]
        return cursor.execute(save_user, values)
    
    def load_user(self, id):
        sql_1 = "SELECT * FROM Users WHERE user_id = ?;"
        rows = cursor.execute(sql_1, str(id)).fetchone()
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

    
        



cooper = User("Cooper", "Tingey", "Provo", "UT", "coopergmail.com", "123", 23, "male")

# cooper_company = Organization(2, "Cooper's cooler company", "Provo", "Utah")

# cooper_company.add_org()
# cooper.show_details()
# cooper.create_user()
# cooper.load_user("1")
cooper.update_email("cooper@gmail.com")
cooper.change_password("asdfasdfasdf")
cooper.save_user()
# cooper.check_pw_match()

connection.commit()  
