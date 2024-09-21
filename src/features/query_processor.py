## query_processor.py


import logging
from utils.decorators import log_exceptions, time_execution
from utils.db_connection import MySQLDatabase
from models.natural_language_to_sql import NaturalLanguageToSQL



class QueryProcessor:
    def __init__(self):
        self.db = MySQLDatabase()
        self.nl_to_sql = NaturalLanguageToSQL()

    @log_exceptions
    @time_execution
    def process_query(self, natural_language_query):
        # 1. Convert natural language to SQL
        sql_query = self.nl_to_sql.translate(natural_language_query)
        logging.info(f"SQL Query: {sql_query}")

        # 2. Execute SQL query
        result = self.db.execute_query(sql_query)

        # 3. Return the result and the generated SQL query
        return {"sql_query": sql_query, "result": result}

    @log_exceptions
    @time_execution
    def close(self):
        # Close the database connection
        self.db.close()
