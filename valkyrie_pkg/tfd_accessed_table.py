#!/usr/bin/env python3
import pandas
import re

def accessedTable(
        data,
        sql,
        verbose):
    """Extract the accessed table from the specified data"""
    # making function more explicit
    data = data
    sql = sql
    verbose = verbose
    
    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracting the accessed table"
        )

    data[sql] = data[sql].astype(str).str.lower()

    # determine the table data was selected from
    data["selected_from"] = data[sql].str.extract(r'(from\s\S*)')
    data["selected_from"] = \
        data["selected_from"].str.replace(
                                    "from ",
                                    "",
                                    regex = False,
        )

    # determine the table data was inserted into
    data["inserted_into"] = data[sql].str.extract(r'(insert\sinto\s\S*)')
    data["inserted_into"] = \
        data["inserted_into"].str.extract('(into\s\S*)')
    data["inserted_into"] = \
        data["inserted_into"].str.extract('(\s\S*)')

    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracted the accessed table\n" \
              + "Merging with original dataset"
        )

    # return dataframe to runtime environment
    return data