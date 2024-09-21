## app.py

import streamlit as st
from features.query_processor import QueryProcessor
from utils.env_setup import load_env
import sys
import os

# Añadir el directorio 'src' al sistema de rutas de Python
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

# Configurar Streamlit
st.title("Natural Language to SQL Interface")
st.write("Enter your query in natural language and get the corresponding SQL query and results from the database.")

# Cargar variables de entorno
load_env()

# Crear instancia del procesador de consultas
query_processor = QueryProcessor()

# Entrada de la consulta en lenguaje natural
natural_language_query = st.text_input("Enter your query in natural language:")

# Botón para ejecutar la consulta
if st.button("Execute Query"):
    if natural_language_query:
        # Procesar la consulta
        with st.spinner('Processing query...'):
            try:
                result = query_processor.process_query(natural_language_query)
                sql_query = result["sql_query"]
                query_result = result["result"]

                # Mostrar la consulta SQL generada
                st.subheader("Generated SQL Query:")
                st.code(sql_query, language='sql')

                # Mostrar el resultado de la consulta
                st.subheader("Query Result:")
                if query_result:
                    st.write(query_result)
                else:
                    st.write("No results found.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query in natural language.")

# Cerrar la conexión a la base de datos después de ejecutar la consulta
query_processor.close()
