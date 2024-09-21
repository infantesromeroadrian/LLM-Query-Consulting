## natural_language_to_sql.py


import openai
import os

class NaturalLanguageToSQL:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def translate(self, natural_language_query):
        messages = [
            {"role": "system", "content": "You are an assistant that translates natural language queries into SQL using the table ClientesVentas with columns: id, nombre, apellidos, edad, marca_producto, importe_vendido."},
            {"role": "user", "content": natural_language_query}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=100,
            temperature=0
        )
        sql_query = response.choices[0].message.content.strip()

        # Clean the query by removing unnecessary characters
        if sql_query.startswith("```sql"):
            sql_query = sql_query[5:]
        if sql_query.endswith("```"):
            sql_query = sql_query[:-3]

        # Remove any leading 'l' character if present
        sql_query = sql_query.lstrip("l").strip()
        return sql_query.strip()
