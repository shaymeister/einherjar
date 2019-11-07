#!/usr/bin/env python3
import pandas
import psycopg2
import sys


def importPostgres(
        connection,
        desiredColumns,
        desiredTable,
        verbose):
    """Import data from a postgres database"""
    # making function more explicit
    address = connection
    desiredColumns = desiredColumns
    desiredTable = desiredTable
    verbose = verbose
    
    # inform user of program progress
    if verbose >= 2:
        print(
            "Attempting to connect to postgres database"
        )

    # attempt to connect to database
    try:
        conn = psycopg2.connect(address)

    # if connection fails, throw exception & terminate program
    except ConnectionError:
        print(
            "Failed to connect to the postgres database"
        )
        sys.exit()

    # -> Export the table to a pandas dataframe
    # use an sql query to extract data from database
    try:
        sql = "select " + desiredColumns + " from " + desiredTable
        data = pandas.read_sql_query(
                            sql,
                            con = conn,
        )
    # if query fails, throw exception & terminate program
    except ImportError:
        print(
            "Failed to query from database"
        )
   
        conn.close()
        sys.exit()

    # 
    #Close communication with the database
    conn.close()

    # inform user of program progress
    if verbose >= 2:
        print(
            "Successfully connected to database"
        )

    # return dataframe to runtime environment
    return