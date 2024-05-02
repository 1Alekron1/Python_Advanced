import requests
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_character_data(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        data = response.json()
        character_data = {
            "name": data["name"],
            "age": data["birth_year"],
            "gender": data["gender"],
        }
        return character_data
    else:
        return None


def store_character_data(character_data):
    if character_data:
        conn = sqlite3.connect("characters.db")
        c = conn.cursor()
        insert_query = "INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)"
        c.execute(
            insert_query,
            (character_data["name"], character_data["age"], character_data["gender"]),
        )
        conn.commit()
        conn.close()


def initialize_database():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS characters (name TEXT, age TEXT, gender TEXT)"
    )
    c.execute(create_table_query)
    conn.commit()
    conn.close()


def download_characters():
    characters = []
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]
    with ThreadPoolExecutor() as executor:
        results = executor.map(fetch_character_data, character_urls)
        for result in results:
            characters.append(result)
            store_character_data(result)
    return characters


def measure_execution_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")


def main():
    initialize_database()
    measure_execution_time(download_characters)


if __name__ == "__main__":
    main()
