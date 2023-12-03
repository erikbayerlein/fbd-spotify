import logging

from psycopg2 import connect


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DataBaseService:
    def __init__(self):
        db_name = "fbd_spotify"
        db_user = "postgres"
        db_password = "postgres"
        db_host = "localhost"
        db_port = "5432"

        try:
            conn = connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
        except Exception as err:
            print(err)

        logger.info("Database connection established")
        self.__connection = conn

    def insert(self, query):
        cursor = self.__connection.cursor()
        sql_query = f"INSERT INTO {query}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as err:
            self.__connection.rollback()
            print(err)
        finally:
            cursor.close()
            self.__connection.close()

    def search(self, query):
        cursor = self.__connection.cursor()
        sql_query = f"SELECT {query}"
        try:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            self.__connection.commit()
        except Exception as err:
            self.__connection.rollback()
            print(err)
        finally:
            cursor.close()
            self.__connection.close()
        return rows

    def delete(self, query):
        cursor = self.__connection.cursor()
        sql_query = f"DELETE FROM {query}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as err:
            self.__connection.rollback()
            print(err)
        finally:
            cursor.close()
            self.__connection.close()

    def update(self, query):
        cursor = self.__connection.cursor()
        sql_query = f"UPDATE {query}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as err:
            self.__connection.rollback()
            print(err)
        finally:
            cursor.close()
            self.__connection.close()

    def close_connection(self):
        self.__connection.close()
