🧠 Natural Language to SQL Query Interface 
🚀 Project: Natural Language to SQL Query Interface This project allows users to make natural language queries that are automatically translated to SQL and executed on a MySQL database. 
We use natural language models (LLMs) via OpenAI and an intuitive user interface developed in Streamlit.

📂 Project Structure
```bash
.
├── assets          # Additional resource files
├── data            # Data for testing and development
├── docs            # Project documentation
├── model           # Trained models or related scripts
├── notebooks       # Jupyter notebooks for testing
├── poetry.lock     # Poetry dependency file
├── pyproject.toml  # Poetry configuration
└── src             # Project source code
    ├── app.py              # Main Streamlit application
    ├── features            # Query processing logic
    ├── models              # Models for NL to SQL translation
    └── utils               # Utilities, DB connections, and decorators
```


https://github.com/infantesromeroadrian/LLM-Query-Consulting/blob/71cdb7000b226f7f5c3d407152b90cb47a1b0132/arquitectura.md


🛠️ Features 🔄 Natural language to SQL translation: 
We use OpenAI models to interpret user questions and convert them into SQL queries. 
🗃️ SQL query execution in MySQL: Direct connection to a MySQL database to execute generated queries and return results. 
🎨 User-friendly interface: 
Streamlit provides a simple and effective interface where users can input queries and see results instantly.

💻 Installation and Setup Clone the repository:

git clone https://github.com/adrianinfantes/LLM-SQL-Query.git
cd natural-language-sql

Install the dependencies using Poetry:
poetry install

Activate the virtual environment:
poetry shell

Run the Streamlit application:
streamlit run src/app.py


Set up the environment: Make sure to create a .env file in the project root with the following variables:

DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=CustomerSales
DB_PORT=3306
OPENAI_API_KEY=your_openai_key

📋 Usage Open the application in your browser (usually at http://localhost:8501). Enter your natural language query, for example: “Show me the names and surnames of customers older than 30 years.” The application will display the generated SQL query and the results obtained from the database.

📚 Example Queries “What is the average importe_vendido?” “List all customers who sold more than 1000 euros.” “Show all customers with marca_producto Apple.”

🚧 Future Improvements 🔍 Support for more database types like PostgreSQL and SQLite. 🌐 Implementation of a module for deeper semantic analysis of queries. 📊 Better visualization of results with interactive charts.

🤝 Contributions Contributions are welcome! If you want to add new features or improve the code, feel free to fork the project and open a pull request.

🛡️ License This project is licensed under the MIT License.

Thank you for visiting our project! 😄✨
