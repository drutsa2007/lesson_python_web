from config import *
from connectDB import create_connection, close_connection

if __name__ == '__main__':
    connection = create_connection('forum', user, password, host, port)
    if connection:
        with connection.cursor() as cursor:
            sql = "CREATE TABLE cars1 (" \
                  "brand VARCHAR(255), " \
                  "model VARCHAR(255), " \
                  "year INT" \
                  ");"
            cursor.execute(sql)
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT table_name FROM information_schema.tables WHERE table_schema "
                "NOT IN ('information_schema','pg_catalog');")
            print(cursor.fetchall())
        close_connection(connection)

