#!/usr/bin/env python3
import os
import sys
import pandas


def importCsv(
        columnNames,
        filePath,
        hasHeaders,
        verbose):
    """Import data from csv file"""
    # making function more explicit
    columnNames = columnNames
    filePath = filePath
    hasHeaders = hasHeaders
    verbose = verbose

    # check if specified file exists
    if os.path.isfile(filePath):
        # inform user of program progress
        if verbose >= 2:
            print(
                "Attempting to read from " + filePath
            )

        # specify the delimiter as ','
        columnNames = columnNames.split(",")

        # if the dataframe has headers
        if hasHeaders:
            # attempt to read csv from file path
            try:
                data = pandas.read_csv(
                            filePath,
                            delimiter = ",",
                            low_memory = False,
                )

            # if read fails, throw exception
            except ImportError:
                print(
                    "Unable to read from the csv:" + filePath
                )

        # if the dataframe doesn't have headers
        else:
            # attempt to read from csv
            try:
                data = pandas.read_csv(
                            filePath,
                            delimiter = ",",
                            names = columnNames,
                            low_memory = False,
                )

             # if read fails, throw exception
            except ImportError:
                print(
                    "Unable to read from the csv:" + filePath
                )

        # inform user of program status        
        if verbose >= 2:
            print(
                "Successfully read from " + filePath
            )
        
        # return dataframe
        return data
    
    # if file at filePath doesn't exist
    else:
        # print the error to the cmd line
        print(
            filePath + " does not exist"
        )

        # terminate the program
        sys.exit()