from datetime import datetime, timedelta
import sqlite3

TOTAL_DAYS = 366
EMPLOYEES_PER_DAY = 10
TOTAL_EMPLOYEES = 366
WORKING_DAYS_PER_EMPLOYEE = TOTAL_DAYS * EMPLOYEES_PER_DAY // TOTAL_EMPLOYEES
WEEKDAYS = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]
ACTIVITIES = ["футбол", "хоккей", "шахматы", "SUP сёрфинг", "бокс", "Dota2", "шах-бокс"]

sql_clear_schedule = """
    DELETE FROM table_friendship_schedule
"""

sql_request_get_all_employees = """
    SELECT id, preferable_sport FROM table_friendship_employees
"""

sql_request_insert_employee = """
    INSERT INTO table_friendship_schedule (employee_id, date)
        VALUES (?,?)
"""


def clear_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute(sql_clear_schedule)


def get_all_employees(cursor: sqlite3.Cursor) -> list:
    return cursor.execute(sql_request_get_all_employees).fetchall()


def insert_schedule(cursor: sqlite3.Cursor, employee_id: int, date: str) -> None:
    cursor.execute(sql_request_insert_employee, (employee_id, date))


def generate_schedule(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    clear_schedule(cursor)
    employees = get_all_employees(cursor)
    working_days = {employee[0]: 0 for employee in employees}
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
    workers_on_day = {start_date + timedelta(days=i): 0 for i in range(TOTAL_DAYS)}
    for day, _ in workers_on_day.items():
        for id, activity in employees:
            if WEEKDAYS[day.weekday()] == WEEKDAYS[ACTIVITIES.index(activity)]:
                continue
            if working_days[id] != WORKING_DAYS_PER_EMPLOYEE + 1:
                insert_schedule(cursor, id, str(day)[:10])
                working_days[id] += 1
                workers_on_day[day] += 1
                if workers_on_day[day] == EMPLOYEES_PER_DAY:
                    break
    conn.commit()


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        generate_schedule(conn)
