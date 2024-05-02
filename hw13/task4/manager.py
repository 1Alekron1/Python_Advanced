import sqlite3

get_worker_salary_query = (
    """SELECT salary FROM 'table_effective_manager' WHERE name = ?"""
)
update_worker_salary_query = (
    """UPDATE 'table_effective_manager' SET salary = ? WHERE name = ?"""
)
delete_worker_query = """DELETE FROM 'table_effective_manager' WHERE name = ?"""


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    cursor.execute(get_worker_salary_query, (name,))
    salary = cursor.fetchone()[0]
    print("Worker's salary:", salary)
    new_salary = salary * 1.10  # Increase salary by 10%
    if new_salary > ivan_sovin_salary:
        cursor.execute(delete_worker_query, (name,))
        print(f"The salary was too high, and worker {name} was dismissed.")
    else:
        cursor.execute(update_worker_salary_query, (new_salary, name))
        print(f"The salary of worker {name} was increased to {new_salary}.")


if __name__ == "__main__":
    with sqlite3.connect("../homework.db") as conn:
        cursor = conn.cursor()
        name = input("Enter the worker's name:\n")
        cursor.execute(get_worker_salary_query, ("Иван Совин",))
        ivan_sovin_salary = cursor.fetchone()[0]
        print("Ivan Sovin's salary:", ivan_sovin_salary)
        ivan_sovin_the_most_effective(cursor, name)
