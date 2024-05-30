import sqlite3
from dataclasses import dataclass
from typing import Optional, Union, List, Dict

DATA = [
    {'id': 0, 'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt'},
    {'id': 1, 'title': 'Clean Code', 'author': 'Robert C. Martin'},
    {'id': 2, 'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen'},
]

DATABASE_NAME = 'table_books.db'
BOOKS_TABLE_NAME = 'books'
AUTHOR_TABLE = 'authors'

@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


@dataclass
class Book:
    title: str
    author: Optional[Union[int, Author]]
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)

def execute_query(query: str, params: tuple = ()) -> None:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

def fetch_query(query: str, params: tuple = ()) -> list:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

def fetch_one_query(query: str, params: tuple = ()) -> Optional[tuple]:
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()

def init_db(initial_records: List[Dict]) -> None:
    create_tables()
    if not is_table_populated(AUTHOR_TABLE):
        populate_authors()
    if not is_table_populated(BOOKS_TABLE_NAME):
        populate_books(initial_records)

def create_tables() -> None:
    execute_query(
        f"""
        CREATE TABLE IF NOT EXISTS '{AUTHOR_TABLE}' (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            middle_name VARCHAR(50)
        );
        """
    )
    execute_query(
        f"""
        CREATE TABLE IF NOT EXISTS `{BOOKS_TABLE_NAME}` (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT,
            author INTEGER REFERENCES '{AUTHOR_TABLE}'(id) ON DELETE CASCADE
        );
        """
    )

def is_table_populated(table_name: str) -> bool:
    result = fetch_one_query(
        f"""
        SELECT EXISTS(SELECT 1 FROM {table_name});
        """
    )
    return result[0] == 1

def populate_authors() -> None:
    execute_query(
        f"""
        INSERT INTO '{AUTHOR_TABLE}' 
            (first_name, last_name, middle_name) VALUES 
            ("Andrew", "Hunt", NULL), 
            ("Robert", "Martin", "C."),
            ("Thomas", "Cormen", "H.")
        """
    )

def populate_books(initial_records: List[Dict]) -> None:
    authors_map = {
        "Andrew Hunt": 1,
        "Robert C. Martin": 2,
        "Thomas H. Cormen": 3
    }
    books = [(item['title'], authors_map[item['author']]) for item in initial_records]
    execute_query(
        f"""
        INSERT INTO `{BOOKS_TABLE_NAME}` (title, author)
        VALUES (?, ?)
        """,
        books
    )

def _get_book_obj_from_row(row: tuple) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])

def _get_author_obj_from_row(row: tuple) -> Author:
    return Author(id=row[0], first_name=row[1], last_name=row[2], middle_name=row[3])

def get_all_books() -> list[Book]:
    rows = fetch_query(f'SELECT * FROM `{BOOKS_TABLE_NAME}`')
    return [_get_book_obj_from_row(row) for row in rows]

def add_book(book: Book) -> Book:
    execute_query(
        f"""
        INSERT INTO `{BOOKS_TABLE_NAME}` (title, author)
        VALUES (?, ?)
        """,
        (book.title, book.author)
    )
    book.id = fetch_one_query('SELECT last_insert_rowid()')[0]
    return book

def update_book(book: Book) -> Book:
    execute_query(
        f"""
        UPDATE `{BOOKS_TABLE_NAME}`
        SET title = ?, author = ?
        WHERE id = ?
        """,
        (book.title, book.author, book.id)
    )
    return book

def get_book_by_id(book_id: int) -> Optional[Book]:
    row = fetch_one_query(
        f"""
        SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE id = ?
        """,
        (book_id,)
    )
    if row:
        return _get_book_obj_from_row(row)

def update_book_by_id(book: Book) -> None:
    execute_query(
        f"""
        UPDATE `{BOOKS_TABLE_NAME}`
        SET title = ?, author = ?
        WHERE id = ?
        """,
        (book.title, book.author, book.id)
    )

def delete_book_by_id(book_id: int) -> None:
    execute_query(
        f"""
        DELETE FROM `{BOOKS_TABLE_NAME}`
        WHERE id = ?
        """,
        (book_id,)
    )

def get_book_by_title(book_title: str) -> Optional[Book]:
    row = fetch_one_query(
        f"""
        SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE title = ?
        """,
        (book_title,)
    )
    if row:
        return _get_book_obj_from_row(row)

def get_author_by_id(id: int) -> Optional[Author]:
    row = fetch_one_query(
        f"""
        SELECT * FROM `{AUTHOR_TABLE}` WHERE id = ?
        """,
        (id,)
    )
    if row:
        return _get_author_obj_from_row(row)

def add_author(author: Author) -> Author:
    execute_query(
        f"""
        INSERT INTO `{AUTHOR_TABLE}`
        (first_name, last_name, middle_name)
        VALUES (?, ?, ?)
        """,
        (author.first_name, author.last_name, author.middle_name)
    )
    author.id = fetch_one_query('SELECT last_insert_rowid()')[0]
    return author

def get_books_by_author(author_id: int) -> list[Book]:
    rows = fetch_query(
        f"""
        SELECT * FROM `{BOOKS_TABLE_NAME}` WHERE author = ?
        """,
        (author_id,)
    )
    return [_get_book_obj_from_row(row) for row in rows]

def delete_author_by_id(id: int) -> None:
    execute_query(
        f"""
        DELETE FROM `{AUTHOR_TABLE}` WHERE id = ?
        """,
        (id,)
    )
