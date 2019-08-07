#!/usr/bin/env python3
import import_csv
import import_postgres 
import import_sqlite3
import sys


def importData(
        column_names,
        connection,
        datatype,
        fpath,
        has_headers,
        desired_columns,
        desired_table,
        verbose):
    """Import data from specified data type"""
    # making function more explicit
    column_names, connection, datatype, fpath, has_headers, \
        desired_columns, desired_table, verbose = \
    column_names, connection, datatype, fpath, has_headers, \
        desired_columns, desired_table, verbose
    if verbose >= 1:
        print("Starting importData()")

# -----> csv data file
    if datatype == 'csv':
        try:
            data = import_csv.importCsv(
                                column_names,
                                fpath,
                                has_headers,
                                verbose)
        except BaseException:
            print("Unable to import data from csv")
            sys.exit()

# -----> postgres database
    elif datatype == 'postgres':
        try:
            data = import_postgres.importPostgres(
                                        connection,
                                        desired_columns,
                                        desired_table,
                                        verbose)
        except BaseException:
            print("Unable to import data from postgres")
            sys.exit()

# -----> sqlitee database
    elif datatype == 'sqlite3':
        try:
            data = import_sqlite3.importSqlite3(
                                    fpath,
                                    has_headers,
                                    verbose)
        except BaseException:
            print("Unable to import data from sqlite3 database")
            sys.exit()

# -----> if unable to connect to database
    else:
        print("Incorrect data type was entered")
        sys.exit()
# -----> return data to runtime environment
    if verbose >= 1:
        print("importData() is now complete")

    return data
