import logging

import pyodbc
from psycopg2 import connect


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DataBaseService:
    def __init__(self):
        db_name = "BDSpotPer2"
        db_driver='SQL Server Native Client 11.0'
        db_server='DESKTOP-ABLPA7D'
        user=None,
        password=None,
        trusted_connection='yes'
        paramater = f"DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};UID={user};PWD={password};TRUSTED_CONNECTION={trusted_connection}"


        try:
            conn = pyodbc.connect(paramater)
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
