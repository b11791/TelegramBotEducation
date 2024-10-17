create_table = """
CREATE TABLE IF NOT EXISTS profile(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cm INTEGER,
    age INTEGER,
    dota_2 TEXT
);
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
