import duckdb
def get_connection():
    return duckdb.connect('my.db')
