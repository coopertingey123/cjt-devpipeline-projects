CREATE TABLE friends (
    friend_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address_city TEXT NOT NULL,
    address_state TEXT NOT NULL,
    phone_number TEXT NOT NULL
);

CREATE TABLE birthday_table (
    friend_id INTEGER PRIMARY KEY,
    place_of_birth TEXT,
    year_of_birth TEXT NOT NULL,
    month_of_birth TEXT NOT NULL,
    FOREIGN KEY (friend_id) REFERENCES friends(friend_id)
);
