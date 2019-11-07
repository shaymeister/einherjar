#!/usr/bin/env python3
import pandas
import sqlite3
import sys
import os 


def importSqlite3(
        columnNames,
        filePath,
        hasHeaders,
        verbose):
    """Import data from user specified sqlite3 database"""
    # making function more explicit
    columnNames = columnNames
    filePath = filePath
    hasHeaders = hasHeaders
    verbose = verbose
    
    # inform user of program progress
    if verbose >= 2:
        print(
            "Attempting to connect to " + filePath
        )

    # check if database exists
    if os.path.isfile(filePath):
        # attempt to connect to database
        try:
            conn = sqlite3.connect(database = filePath)
        
        # if connection fails, throw exception & terminate program
        except ConnectionError:
            print(
                "Failed to connect to " + filePath
            )
            sys.exit()

        # inform user of program progress
        if verbose >= 2:
            print(
                "Successfully connected to " + filePath
            )

        # if dataframe as column headers
        if hasHeaders:
            # attempt to connect to database
            try:
                data = pandas.read_sql(
                                "SELECT * FROM logs",
                                conn,
                )

            # if connection fails, throw exception & terminate program
            except BaseException:
                sys.exit()

        # if dataframe doesn't have column headers
        else:
            # attempt to connect to database
            try:
                data = pandas.read_sql(
                                "SELECT * FROM logs",
                                conn,
                                columns = columnNames,
                )
            # if connection fails, throw exception and terminate program
            except ImportError:
                sys.exit()

            # return dataframe to runtime environment
            return data
        
    # if database doesn't exist, throw exception & terminate program
    else:
        print(
            filePath + " does not exist"
        )
        sys.exit()