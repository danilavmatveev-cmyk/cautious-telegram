from typing import List, Tuple
import sqlite3
def select_year() -> List[Tuple]:

    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM films WHERE year > ?', (2000,))


    films = cursor.fetchall()
    return films
