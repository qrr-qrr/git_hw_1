import duckdb
import pandas as pd
def get_data(query):
    conn = duckdb.connect('my.db')
    return conn.execute(query).df()
