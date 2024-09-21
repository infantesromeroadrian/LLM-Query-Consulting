## env_setup.py


import os
from dotenv import load_dotenv
from pathlib import Path

def load_env():
    # Specify the path to .env file in the project root
    env_path = Path('../.env')
    load_dotenv(dotenv_path=env_path)

    # Check if the environment variables are loaded
    db_name = os.getenv('DB_NAME')
    if db_name is None:
        raise EnvironmentError("Error: Could not load .env file or DB_NAME is not defined")
    else:
        print(f"Loaded database name: {db_name}")
