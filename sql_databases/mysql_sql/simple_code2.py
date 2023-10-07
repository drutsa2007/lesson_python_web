import pymysql
import pymysql.cursors

config = {
    'user': 'root',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': 3306,  # не строка!
    'database': 'blog',
    'cursorclass': pymysql.cursors.DictCursor
}


def create_connection():
    connection = None
    try:
        connection = pymysql.connect(**config)
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
        print(1)
        # данная штука для работы с БД, для работы с таблицей не требуется
        # conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with conn.cursor() as cursor:
            sql = """
            CREATE TABLE users1 (
              id bigint PRIMARY KEY AUTO_INCREMENT, 
              caption varchar(255)
            );
            """
            cursor.execute(sql)
            conn.commit()
        close_connection(conn)
