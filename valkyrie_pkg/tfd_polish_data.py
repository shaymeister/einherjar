#!/usr/bin/env python3
import pandas


def polishData(
        cmdTag,
        data,
        id1,
        id2,
        sql,
        verbose):
    """Clean up the data after transformation"""
    # making functions more explicit
    cmdTag = cmdTag
    data = data
    id1 = id1
    id2 = id2
    sql = sql
    verbose = verbose
    
    # inform user of program progress
    if verbose >= 2:
        print(
            "Data is being polished"
        )

    # clean up the data after its evolution
    data[sql].astype(str)
    data = data.loc[data[sql].str.contains('execute')]
    data['total_duration'].dropna().astype(float)
    data = data.drop_duplicates([id1, id2], keep='first')
    data = data.loc[(data[cmdTag] == 'SELECT') | (data[cmdTag] == 'INSERT') |
                    (data[cmdTag] == 'BIND') | (data[cmdTag] == 'PARSE')]

    # inform user of program progress
    if verbose >= 2:
        print(
            "Data has been polished"
        )

    # return dataframe to runtime environment
    return data