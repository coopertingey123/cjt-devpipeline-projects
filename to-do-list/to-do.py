import csv
import sqlite3

connection = sqlite3.connect('to_do_list.db')
cursor = connection.cursor()

class User:
    def __init__(self):
        # self.first_name = input("Enter new user first name. Enter: ")
        # self.last_name = input("Enter new user last name. Enter: ")
        return

    
    def write_user_csv(self):
        with open("users.csv", "a") as user_file:
            writer = csv.writer(user_file)
            writer.writerow([self.first_name, self.last_name])

    def add_user_sql(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        sql_statement = """
            INSERT INTO Users (
                first_name, last_name
            )
            VALUES (
                ?, ?
            )
        """
        values = self.first_name, self.last_name
        return cursor.execute(sql_statement, values)
    
    def read_user_csv(self):
        with open("users.csv", "r") as user_csv:
            reader = csv.reader(user_csv)
            for row in reader:
                print(row)
        return
    
    def read_user_sql(self):
        sql_statement = """
            SELECT * FROM Users
        """
        users = cursor.execute(sql_statement).fetchall()
        print("\nUser ID     First Name   Last Name")
        for user in users:
            print(f"{user[0]:<11} {user[1]:<12} {user[2]}")
        print("\n")

    def delete_user(self):
        print(User.read_user_sql(self))
        select_user = input("Select the user ID of the user you would like to delete. Enter: ")
        sql_statement = """
            DELETE FROM Users
            WHERE user_id = ?
        """
        return cursor.execute(sql_statement, select_user)


class ToDoTask(User):
    def __init__(self):
        self.task = input("Enter the task: ")

    def write_todo_sql(self):
        users = User.read_user_sql(self)
        print(users)
        user_id = input("Select user ID you'd like to pair your task to. Enter: ")
        sql_statement = """
            INSERT INTO to_do_list (
                task, user_id, completed
            )
            VALUES (
                ?, ?, ?
            )
        """
        values = self.task, user_id, 0
        return cursor.execute(sql_statement, values)


    def write_todo_csv(self):
        with open("to-do.csv", "a") as to_do_file:
            writer = csv.writer(to_do_file)
            writer.writerow([self.task])

    def read_todo_sql(self):
        sql_statement = """
            SELECT * FROM to_do_list
        """
        return cursor.execute(sql_statement).fetchall()
    
    def read_todo_csv(self):
        with open("to-do.csv", "r") as todo_csv:
            reader = csv.reader(todo_csv)
            for row in reader:
                print(row)
        return

    def see_tasks_user(self):
        users = User.read_user_sql(self)
        print(users)
        select_user = input("Select the user ID to see their tasks. Enter: ")
        sql_statement = """
            SELECT task_id, task, completed FROM to_do_list
            WHERE user_id = ?
        """
        user_tasks = cursor.execute(sql_statement, select_user).fetchall()
        print("Task ID     Task                 Completed (0=no, 1=yes)")
        for task in user_tasks:
            print(f"{task[0]:<11} {task[1]:<20} {task[2]}")

# To do:
# Ability to complete a task
# Read functions only return uncompleted tasks
# Ability to see tasks





    

            

cooper = User()
# james = User("James", "Wright")
# print(cooper.read_user_sql())
# james.add_user_sql()
# james.write_user_csv()
# laundry = ToDoTask("do the laundry")
# print(laundry.read_todo_sql())
# laundry.read_todo_csv()

# cooper.read_user_sql()
# User().add_user_sql()
ToDoTask().see_tasks_user()



connection.commit()  