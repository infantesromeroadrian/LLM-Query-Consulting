# src/model/nl_to_sql.py
from openai import OpenAI
import logging
from utils.decorators import log_exceptions


class NaturalLanguageToSQL:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("Se requiere una API key de OpenAI válida")
        self.client = OpenAI(api_key=api_key)

    @log_exceptions
    def translate(self, natural_language_query):
        messages = [
            {"role": "system",
             "content": "Eres un asistente que traduce consultas en lenguaje natural a SQL usando la tabla ClientesVentas, que contiene las columnas: id, nombre, apellidos, edad, marca_producto e importe_vendido."},
            {"role": "user", "content": natural_language_query}
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=100,
            temperature=0
        )

        sql_query = response.choices[0].message.content.strip()

        # Limpiar la consulta eliminando caracteres innecesarios
        if sql_query.startswith("```sql"):
            sql_query = sql_query[5:]
        if sql_query.endswith("```"):
            sql_query = sql_query[:-3]

        # Eliminar caracteres adicionales que puedan estar fuera de lugar
        sql_query = sql_query.lstrip("l").strip()

        return sql_query.strip()