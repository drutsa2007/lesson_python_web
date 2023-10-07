import mysql.connector

config = {
    'user': 'root',
    'password': 'admin',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'blog',
    'raise_on_warnings': True
}


def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**config)
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
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetch()
            for record in result:
                print("{}".format(record))
        close_connection(conn)
