
CREATE TABLE IF NOT EXISTS 'actors' (
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50) NOT NULL,
    act_last_name VARCHAR(50) NOT NULL,
    act_gender VARCHAR(1) NOT NULL
);

INSERT INTO "actors" (act_first_name, act_last_name, act_gender) VALUES
                    ("Алексей", "Алексеев", "М"), ("Мария", "Маркова", "Ж");

CREATE TABLE IF NOT EXISTS 'movie' (
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50) NOT NULL
);

INSERT INTO "movie" (mov_title) VALUES ("Комедия 1"), ("Драма 2");

CREATE TABLE IF NOT EXISTS 'director' (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_last_name VARCHAR(50) NOT NULL
);

INSERT INTO 'director' (dir_first_name, dir_last_name) VALUES
        ("Анна", "Кузнецова"), ("Сергей", "Петров");

CREATE TABLE IF NOT EXISTS "movie_cast" (
  act_id INTEGER REFERENCES actors(act_id),
  mov_id INTEGER REFERENCES movie(mov_id),
  role VARCHAR(50) NOT NULL
);

INSERT INTO movie_cast (act_id, mov_id, role) VALUES
(1, 1, "Главная роль"), (2, 2, "Второстепенная роль");

CREATE TABLE IF NOT EXISTS 'oscar_awarded' (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id INTEGER REFERENCES movie(mov_id)
);

INSERT INTO oscar_awarded (mov_id) VALUES
(1), (2);

CREATE TABLE IF NOT EXISTS 'movie_direction' (
    dir_id INTEGER REFERENCES director(dir_id),
    mov_id INTEGER REFERENCES movie(mov_id)
);

INSERT INTO movie_direction (dir_id, mov_id) VALUES
    (1, 1), (2, 2);
