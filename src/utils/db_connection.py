## db_connection.py


import mysql.connector
import os
import logging
from utils.decorators import log_exceptions, time_execution

class MySQLDatabase:
    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.port = os.getenv('DB_PORT')
        self.connection = None

    @log_exceptions
    @time_execution
    def connect(self):
        logging.info("Connecting to MySQL database...")
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        logging.info("Successfully connected to the database.")

    @log_exceptions
    @time_execution
    def execute_query(self, query):
        if self.connection is None:
            self.connect()
        logging.info(f"Executing query: {query}")
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        logging.info("Query executed successfully.")
        return result

    @log_exceptions
    @time_execution
    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Connection closed.")
