import psycopg2  # v.2.9.7
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database="blog",
            user='postgres',
            password='admin',
            host='127.0.0.1',
            port='5432',
        )
        print("Подключение к базе данных PostgreSQL прошло успешно")
    except Exception as e:
        print(f"Произошла ошибка:\n{e}")
    return connection


def close_connection(connection):
    connection.close()
    print("Соединение закрыто")


if __name__ == '__main__':
    conn = create_connection()
    if conn:
        # данная штука для работы с БД, для работы с таблицей не требуется
        # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cursor:
            sql = "CREATE TABLE users (" \
                  "brand VARCHAR(255), " \
                  "model VARCHAR(255), " \
                  "year INT" \
                  ");"
            cursor.execute(sql)
            conn.commit()
    close_connection(conn)
