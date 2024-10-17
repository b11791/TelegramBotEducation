from stickers_bot import sql_queries
from stickers_bot.db import SQLite

if __name__ == '__main__':
    with SQLite() as db:
        result = db.cursor.execute(sql_queries.select_users).fetchall()
        max_cm = max(user["cm"] for user in result)
