from config import *
import psycopg2  # v.2.9.7


def create_connection(db_name, db_user, db_password, db_host, db_port):
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Подключение к базе данных PostgreSQL прошло успешно")

        return connection
        # with connection.cursor() as cursor:
        #     pass
    except Exception as e:
        print(f"Произошла ошибка:\n{e}")
        return False


def close_connection(connection):
    connection.close()
    print("Соединение закрыто")


if __name__ == '__main__':
    conn = create_connection("qqq", user, password, host, port)
    print(conn)
    close_connection(conn)
