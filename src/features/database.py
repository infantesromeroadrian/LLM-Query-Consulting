# src/features/database.py
import mysql.connector
import os
import logging
from utils.decorators import time_execution, log_exceptions
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

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
        if self.connection is not None and self.connection.is_connected():
            logging.info("Already connected to the database.")
            return
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
    def execute_query(self, query, params=None):
        if self.connection is None or not self.connection.is_connected():
            self.connect()
        logging.info(f"Executing query: {query}")
        cursor = self.connection.cursor(dictionary=True)  # Using dictionary cursor for better handling
        cursor.execute(query, params)
        result = cursor.fetchall()
        logging.info("Query executed successfully.")
        cursor.close()
        return result

    @log_exceptions
    @time_execution
    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logging.info("Connection closed.")