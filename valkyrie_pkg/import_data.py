#!/usr/bin/env python3
import sys

from valkyrie_pkg import import_csv
from valkyrie_pkg import import_postgres 
from valkyrie_pkg import import_sqlite3


def importData(
        columnNames,
        connection,
        desiredColumns,
        desiredTable,
        filePath,
        hasHeaders,
        importDataType,
        verbose):
    """Import data from specified data type"""
    # making function more explicit
    columnNames = columnNames
    connection = connection
    desiredColumns = desiredColumns
    desiredTable = desiredTable
    filePath = filePath
    hasHeaders = hasHeaders
    importDataType = importDataType
    verbose = verbose
    
    # inform user of program progress
    if verbose >= 1:
        print(
            "Starting importData()"
        )

# -----> csv data file
    if importDataType == "csv":
        # attempt to import data using importCsv() function
        try:
            data = import_csv.importCsv(
                                columnNames,
                                filePath,
                                hasHeaders,
                                verbose,
            )

        # if import fails, throw exception & terminate the program
        except ImportError:
            print(
                "Unable to import data from csv"
            )
            sys.exit()

# -----> postgres database
    elif importDataType == "postgres":
        # attempt to import data using importPostgres() function
        try:
            data = import_postgres.importPostgres(
                                        connection,
                                        desiredColumns,
                                        desiredTable,
                                        verbose,
            )

        # if import fails, throw exception & terminate program
        except ImportError:
            print(
                "Unable to import data from postgres"
            )
            sys.exit()

# -----> sqlitee database
    elif importDataType == "sqlite3":
        # attempt to import data using importSqlite3() function
        try:
            data = import_sqlite3.importSqlite3(
                                    columnNames,
                                    filePath,
                                    hasHeaders,
                                    verbose,
            )

        # if import fails, throw exception and terminate program
        except ImportError:
            print(
                "Unable to import data from sqlite3 database"
            )
            sys.exit()

# -----> if unable to connect to database, throw exception & terminate program
    else:
        print(
            "Incorrect data type was entered"
        )
        sys.exit()

    # inform user of program progress
    if verbose >= 1:
        print(
            "importData() is now complete"
        )

    # return dataframe to runtime environment
    return data