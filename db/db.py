import os
import psycopg2
import psycopg2.extras

DB_URL = f"dbname={os.environ.get('DATABASE_URL')}"

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL) # open connection
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # we use cursor to run SQL commands
    cursor.execute(query, parameters) # begin transaction
    if query.strip().lower().startswith("select"):
        results = cursor.fetchall()
    else:
        results = None
    connection.commit() # end transaction
    connection.close() # close connection
    return results