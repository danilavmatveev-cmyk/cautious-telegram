def create_cinema_database():
    import sqlite3
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS films (id INTEGER,
    title TEXT NOT NULL,
    director TEXT,
    year INTEGER
    )
    ''')
create_cinema_database()