import os
import logging

from psycopg2 import connect


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class DataBaseService:
    def __init__(self):
        db_name = os.getenv("DB_NAME")
        if db_name is None:
            logger.error("DB_NAME is not defined")

        db_user = os.getenv("DB_USER")
        if db_user is None:
            logger.error("DB_USER is not defined")

        db_password = os.getenv("DB_PASSWORD")
        if db_password is None:
            logger.error("DB_PASSWORD is not defined")

        db_host = os.getenv("DB_HOST")
        if db_host is None:
            logger.error("DB_HOST is not defined")

        db_port = os.getenv("DB_PORT")
        if db_port is None:
            logger.error("DB_PORT is not defined")

        try:
            conn = connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
        except Exception as ex:
            logger.error(
                f"Unable to establish connection to the database: {str(ex)}"
            )

        logger.info("Database connection established")
        self.__connection = conn

    def insert_blobs(self, key, byte_value):
        cursor = self.__connection.cursor()
        sql_query = "INSERT INTO "+ table_name +" (nome, dados) VALUES (%s, %s)"
        try:
            cursor.execute(sql_query, (key, byte_value))
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise DataInspectionLambdaException(
                f"Error trying insert blobs of '{key}' - {e}"
            )
        finally:
            cursor.close()

    def delete_registers(self):
        cursor = self.__connection.cursor()
        sql_query = f"DELETE FROM {table_name}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as e:
            self.__connection.rollback()
            raise DataInspectionLambdaException(
                f"Error trying clean table '{table_name}' - {e}"
            )
        finally:
            cursor.close()

    def close_connection(self):
        self.__connection.close()
