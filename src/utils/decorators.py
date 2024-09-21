## decorators.py


import logging
import time
from functools import wraps

# Decorador para medir el tiempo de ejecución de las funciones
def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Decorador para capturar excepciones y registrarlas
def log_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error occurred in function '{func.__name__}': {e}")
            raise e
    return wrapper
