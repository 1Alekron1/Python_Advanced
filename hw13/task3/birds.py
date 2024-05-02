import datetime
import sqlite3

check_availability_query = """
SELECT EXISTS(SELECT * FROM 'birds' WHERE bird_name = ?)
"""

add_bird_query = """ 
INSERT INTO 'birds' (bird_name, time) VALUES (?, ?);
"""


def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    cursor.execute(add_bird_query, (bird_name, date_time))
    print(f"Bird '{bird_name}' logged.")


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(check_availability_query, (bird_name,))
    result = cursor.fetchone()
    return result[0]


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor = conn.cursor()
        bird_name = input("Enter the bird's name:\n").lower()
        if not check_if_such_bird_already_seen(cursor, bird_name):
            log_bird(cursor, bird_name, str(datetime.datetime.now().time()))
        else:
            print(f"{bird_name} is already logged.")
