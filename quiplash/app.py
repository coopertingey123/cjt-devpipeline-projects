import sqlite3
connection = sqlite3.connect("quiplash.db")
cursor = connection.cursor()

def create_table():
    with open("create_table.sql") as sql_file:
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)

# create_table()

def pull_questions():
    with open("get_questions.sql") as sql_file:
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)



connection.commit()  

# Quiplash is a game that has different parts:
# 1. Enter a game with a game code
# 2. When the game starts, each player is given 2 questions that are generated randomly
# (Each question is given to two players)
# 3. They then answer those questions
# 4. The questions are then shown, along with the answers
# 5. Each player votes on which answer is funnier
# 6. Players are given points based on how many votes they got 
# 7. There are 3 rounds of this, and the winner is the one with the most points at the end