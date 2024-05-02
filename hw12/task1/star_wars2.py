import requests
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


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


def save_character_data_to_db(character_data):
    if character_data:
        conn = sqlite3.connect("characters.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)",
            (character_data["name"], character_data["age"], character_data["gender"]),
        )
        conn.commit()
        conn.close()


def create_database_if_not_exists():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS characters (name TEXT, age TEXT, gender TEXT)"
    )
    conn.commit()
    conn.close()


def download_characters_with_thread_pool():
    characters = []
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]

    with ThreadPoolExecutor() as executor:
        results = executor.map(fetch_character_data, character_urls)

        for result in results:
            characters.append(result)
            save_character_data_to_db(result)

    return characters


def download_characters_with_process_pool():
    characters = []
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]

    with Pool() as pool:
        results = pool.map(fetch_character_data, character_urls)

        for result in results:
            characters.append(result)
            save_character_data_to_db(result)

    return characters


def measure_time_execution(func, pool_type):
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"Execution time ({pool_type}): {end_time - start_time} seconds")


def main():
    create_database_if_not_exists()
    measure_time_execution(download_characters_with_thread_pool, "ThreadPoolExecutor")
    measure_time_execution(download_characters_with_process_pool, "Pool")


if __name__ == "__main__":
    main()
