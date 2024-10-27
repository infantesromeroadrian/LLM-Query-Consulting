# main.py
import logging
from features.database import MySQLDatabase
from model.nl_to_sql import NaturalLanguageToSQL
from utils.decorators import time_execution, log_exceptions

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Clase principal para gestionar el flujo completo
class QueryProcessor:
    def __init__(self):
        self.db = MySQLDatabase()
        self.nl_to_sql = NaturalLanguageToSQL()

    @log_exceptions
    @time_execution
    def process_query(self, natural_language_query):
        # 1. Convertir el lenguaje natural a SQL
        sql_query = self.nl_to_sql.translate(natural_language_query)
        logging.info(f"SQL Query: {sql_query}")

        # 2. Ejecutar la consulta SQL
        result = self.db.execute_query(sql_query)

        # 3. Devolver el resultado y la consulta SQL generada
        return {"sql_query": sql_query, "result": result}

    @log_exceptions
    @time_execution
    def close(self):
        # Cerrar la conexión a la base de datos
        self.db.close()


if __name__ == "__main__":
    # Crear instancia del procesador de consultas
    query_processor = QueryProcessor()

    # Your natural language query
    natural_language_query = "Show me average importe_vendido of customers"

    # Procesar la consulta
    result = query_processor.process_query(natural_language_query)
    logging.info(f"SQL Query: {result['sql_query']}")
    logging.info(f"Query Result: {result['result']}")

    # Another natural language query
    natural_language_query = "Show me the names and surnames of customers older than 30 years and who sold more than 1000 euros."

    # Procesar la consulta
    result = query_processor.process_query(natural_language_query)
    logging.info(f"SQL Query: {result['sql_query']}")
    logging.info(f"Query Result: {result['result']}")

    # Cerrar la conexión
    query_processor.close()
