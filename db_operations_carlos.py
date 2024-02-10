#Import dependencies
import pathlib
import sqlite3
import pandas as pd
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method


def execute_sql_from_file(db_filepath, sql_file):
    logging.debug("Starting Major Function")
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
    logging.debug("ending major function")

def main():
    logging.debug("Starting Major Function")
    db_filepath = 'your_database.db'

    db_filepath = pathlib.Path("project.db")
    update_records = pathlib.Path("sql", "update_records.sql")
    insert_records = pathlib.Path("sql", "insert_records.sql")
    delete_records = pathlib.Path("sql", "delete_records.sql")
    query_aggregation = pathlib.Path("sql", "query_aggregation.sql")
    query_filter = pathlib.Path("sql", "query_filter.sql")
    query_sorting = pathlib.Path("sql", "query_sorting.sql")
    query_group_by = pathlib.Path("sql", "query_group_by.sql")
    query_join = pathlib.Path("sql", "query_join.sql")

    #Create database schema and populate with data
    execute_sql_from_file(db_filepath, insert_records)
    logging.info("Inserted Records") # Log record insertion

    execute_sql_from_file(db_filepath, update_records)
    logging.info("Updated Records") # Log record updates

    execute_sql_from_file(db_filepath, delete_records)
    logging.info("Deleted Records") # Log record deletion

    execute_sql_from_file(db_filepath, query_aggregation)
    logging.info("Executed Aggregation Query") # Log aggregation query 

    execute_sql_from_file(db_filepath, query_filter)
    logging.info("Executed Filter Query") # Log filter query 

    execute_sql_from_file(db_filepath, query_sorting)
    logging.info("Executed Sorting Query") # Log sorting query

    execute_sql_from_file(db_filepath, query_group_by)
    logging.info("Executed Group by Query") # Log group by query

    execute_sql_from_file(db_filepath, query_join)
    logging.info("Executed join Query") # Log join query

    logging.info("All SQL operations completed successfully")
    logging.debug("Ending major_function")


logging.info("Program ended")  # add this at the end of the main method

if __name__ == "__main__":
    main()