# src/app.py
import streamlit as st
import pandas as pd
from features.database import MySQLDatabase
from model.nl_to_sql import NaturalLanguageToSQL
from utils.decorators import log_exceptions, time_execution
import logging
import os
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cargar variables de entorno
load_dotenv()

# Configurar la página de Streamlit
st.set_page_config(
    page_title="Consultas SQL en Lenguaje Natural",
    page_icon="🔍",
    layout="wide"
)


class StreamlitApp:
    def __init__(self, openai_api_key):
        self.db = MySQLDatabase()
        self.nl_to_sql = NaturalLanguageToSQL(openai_api_key)

    @log_exceptions
    def process_query(self, natural_language_query):
        # Convertir lenguaje natural a SQL
        sql_query = self.nl_to_sql.translate(natural_language_query)

        # Ejecutar la consulta SQL
        result = self.db.execute_query(sql_query)

        return sql_query, result


def main():
    # Título y descripción
    st.title("🔍 Consultor de Base de Datos en Lenguaje Natural")

    # Configuración de la API key
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Pegue su API key de OpenAI aquí (sk-...)",
        help="Puede obtener su API key desde https://platform.openai.com/account/api-keys",
        value=os.getenv("OPENAI_API_KEY", "")
    )

    if not openai_api_key:
        st.warning("Por favor, introduce tu API key de OpenAI para continuar.")
        st.stop()

    # Información sobre la base de datos
    st.markdown("""
    Esta aplicación te permite consultar la base de datos usando lenguaje natural.
    La tabla disponible es **ClientesVentas** con las siguientes columnas:
    - id
    - nombre
    - apellidos
    - edad
    - marca_producto
    - importe_vendido
    """)

    # Inicializar la aplicación
    try:
        app = StreamlitApp(openai_api_key)

        # Área de entrada de texto
        query = st.text_area(
            "Escribe tu consulta en lenguaje natural:",
            placeholder="Ejemplo: Muéstrame los clientes que han comprado más de 1000 euros",
            height=100
        )

        # Botón para ejecutar la consulta
        if st.button("Ejecutar Consulta", type="primary"):
            if query:
                try:
                    # Mostrar spinner mientras se procesa la consulta
                    with st.spinner("Procesando tu consulta..."):
                        # Procesar la consulta
                        sql_query, results = app.process_query(query)

                    # Mostrar la consulta SQL generada
                    st.subheader("Consulta SQL Generada:")
                    st.code(sql_query, language="sql")

                    # Mostrar los resultados
                    st.subheader("Resultados:")
                    if results:
                        # Convertir los resultados a un DataFrame de pandas
                        df = pd.DataFrame(results)

                        # Mostrar el número total de resultados
                        st.markdown(f"*Se encontraron {len(df)} resultados*")

                        # Mostrar los datos en una tabla
                        st.dataframe(
                            df,
                            use_container_width=True,
                            hide_index=True
                        )

                        # Añadir opción para descargar los resultados
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Descargar resultados como CSV",
                            data=csv,
                            file_name="resultados_consulta.csv",
                            mime="text/csv"
                        )
                    else:
                        st.info("La consulta no devolvió ningún resultado.")

                except Exception as e:
                    st.error(f"Error al procesar la consulta: {str(e)}")
            else:
                st.warning("Por favor, introduce una consulta.")

        # Ejemplos de consultas
        with st.expander("Ver ejemplos de consultas"):
            st.markdown("""
            - Muestra todos los clientes mayores de 30 años
            - ¿Cuál es el promedio de ventas por marca de producto?
            - Lista los nombres y apellidos de los clientes que han comprado más de 5000 euros
            - ¿Cuántos clientes hay por rango de edad (20-30, 31-40, 41-50, >50)?
            - Muestra las 5 ventas más altas
            """)

    except Exception as e:
        st.error(f"Error al inicializar la aplicación: {str(e)}")

    # Footer con información adicional
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center'>
            <p>Desarrollado con ❤️ usando Streamlit y OpenAI</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()