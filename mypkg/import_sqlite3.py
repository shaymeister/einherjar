#!/usr/bin/env python3
import pandas
import sqlite3
import sys
import os 


def importSqlite3(
        fpath,
        has_headers,
        verbose):
    """Import data from user specified sqlite3 database"""
    # making function more explicit
    fpath, has_headers, verbose = \
        fpath, has_headers, verbose
    if verbose >= 2:
        print("Attempting to connect to " + fpath)
    if os.path.isfile(fpath):
        try:
            conn = sqlite3.connect(database=fpath)
        except BaseException:
            print("Failed to connect to " + fpath)
            sys.exit()
        if verbose >= 2:
            print('Successfully connected to ' + fpath)
        if has_headers == True:
            try:
                data = pandas.read_sql('SELECT * FROM logs', conn)
            except BaseException:
                sys.exit()
        else:
            try:
                data = pandas.read_sql(
                    'SELECT * FROM logs', conn, columns=column_names)
            except BaseException:
                sys.exit()

            return data
    else:
        print(fpath + " does not exist")
        sys.exit()
