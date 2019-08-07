#!/usr/bin/env python3
import os
import sys
import pandas


def importCsv(
        column_names,
        fpath,
        has_headers,
        verbose):
    """Import data from csv file"""
    # making function more explicit
    column_names, fpath, has_headers, verbose = \
        column_names, fpath, has_headers, verbose
    if os.path.isfile(fpath):
        if verbose >= 2:
            print("Attempting to read from " + fpath)
        column_names = column_names.split(",")
        if has_headers == True:
            try:
                data = pandas.read_csv(fpath, delimiter=',', low_memory=False)
            except BaseException:
                print('Unable to read from the csv:' + fpath)

        else:
            data = pandas.read_csv(fpath, delimiter=',',
                                   names=column_names, low_memory=False)
        if verbose >= 2:
            print("Successfully read from " + fpath)
        return data
    else:
        print(fpath + " does not exist")
        sys.exit()
