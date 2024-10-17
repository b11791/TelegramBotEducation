# ОБРАЩЕНИЕ К БД

1. Напиши sql запрос в sql_queries.py
```python
select_users = """
SELECT *
FROM profile
"""
```
2. Используй запрос отак:

    2.1. SELECT
    ```python
    # Получение максимальных см
    with SQLite() as db:
        result = db.cursor.execute(sql_queries.select_users).fetchall()
        max_cm = max(user["cm"] for user in result)
    ```
    2.2. INSERT / UPDATE / DELETE
    ```python
    # Получение максимальных см
    with SQLite() as db:
        db.cursor.execute(sql_queries.ZAPROS)
        db.connection.commit()
    ```
