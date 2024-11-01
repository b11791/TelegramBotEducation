create_table_user = """
CREATE TABLE IF NOT EXISTS profile(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cm INTEGER,
    age INTEGER,
    dota_2 TEXT
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
    name TEXT,
    category_id INTEGER, 
    FOREIGN KEY (category_id) REFERENCES category (id)
);
"""

create_table_stickers = """
CREATE TABLE IF NOT EXISTS stickers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_code TEXT,
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
INSERT INTO profile(name, cm, age, dota_2)
VALUES ('Denis', 9999, 16, 'gay')
"""

create_super_user_2 = """
INSERT INTO profile(name, cm, age, dota_2)
VALUES ('Vladimir', 9999, 22, 'gay')
"""

select_users = """
SELECT *
FROM profile
"""
