CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL
)

CREATE TABLE answers (
    answer_id,
    question_id,
    player_id,
    answer
)

CREATE TABLE session (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_code TEXT NOT NULL
)

CREATE TABLE session_players (
    player_id,
    session_id
)

CREATE TABLE scores (
    player_id,
    session_id,
    score
)

CREATE TABLE questions (
    question_id,
    question
)


session table

questions table
-question_id
-question
-

