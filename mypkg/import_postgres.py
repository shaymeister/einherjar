#!/usr/bin/env python3
import pandas
import psycopg2
import sys


def importPostgres(
        connection,
        desired_columns,
        desired_table,
        verbose,):
    """Import data from a postgres database"""
    # making function more explicit
    connection, desired_columns, desired_table, verbose = \
        connection, desired_columns, desired_table, verbose
    if verbose >= 2:
        print("Attempting to connect to postgres database")
    # -> Connect to an existing database
    address = connection
    try:
        conn = psycopg2.connect(address)
    except:
        print("Failed to connect to the postgres databse")
        sys.exit()
    # -> Export the table to a pandas dataframe
    try:
        sql = "select " + desired_columns + " from " + desired_table
        data = pandas.read_sql_query(sql, con=conn)
    except:
        print("Failed to query from database")
        conn.close()
        sys.exit()
    # Close communication with the database
    conn.close()
    if verbose >= 2:
        print("Successfully connected to database")
    return data
