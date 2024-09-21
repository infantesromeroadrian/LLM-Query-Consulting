import logging
from utils.env_setup import load_env
from features.query_processor import QueryProcessor

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_env()

# Create an instance of the query processor
query_processor = QueryProcessor()

# Process the first query
natural_language_query = "Show me average importe_vendido of customers"
result = query_processor.process_query(natural_language_query)
print(f"SQL Query: {result['sql_query']}")
print(f"Query Result: {result['result']}")

# Process the second query
natural_language_query = "Show me the names and surnames of customers older than 30 years and who sold more than 1000 euros."
result = query_processor.process_query(natural_language_query)
print(f"SQL Query: {result['sql_query']}")
print(f"Query Result: {result['result']}")

# Close the connection
query_processor.close()