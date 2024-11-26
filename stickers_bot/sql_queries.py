create_table_user = """
CREATE TABLE IF NOT EXISTS profile(
    tg_id INTEGER PRIMARY KEY,
    name TEXT,
    cm INTEGER,
    age INTEGER,
    is_admin BOOL DEFAULT 0
);
"""

create_table_category = """CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
"""


create_table_stickerpacks = """
CREATE TABLE IF NOT EXISTS stickerpacks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    category_id INTEGER, 
    FOREIGN KEY (category_id) REFERENCES category (id)
);
"""

create_table_stickers = """
CREATE TABLE IF NOT EXISTS stickers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_code TEXT UNIQUE,
    stickerpack_id INTEGER, 
    FOREIGN KEY (stickerpack_id) REFERENCES stickerpacks (id)
);
"""

create_categories = """
INSERT INTO category (id, name)
VALUES(1, "упоротые"),
(2, "пошлые"),
(3, "смешные"),
(4, "конченные")
ON CONFLICT(id) 
DO NOTHING;
"""

create_super_user = """
INSERT INTO profile(tg_id, name, cm, age, is_admin)
VALUES (1031726737, 'Denis', 9999, 16, 1)
ON CONFLICT(tg_id) 
DO NOTHING;
"""

select_users = """
SELECT *
FROM profile
"""


select_user_id = """
SELECT 1
FROM profile
WHERE tg_id = {} 
"""


insert_user = """
INSERT INTO profile(tg_id, name, cm, age)
VALUES ({}, '{}', {}, {})
ON CONFLICT(tg_id) 
DO NOTHING;
"""

select_user_info = """
SELECT name, age, cm
FROM profile 
WHERE tg_id = {}
"""