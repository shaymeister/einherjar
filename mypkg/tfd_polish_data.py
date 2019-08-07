#!/usr/bin/env python3
import pandas


def polishData(
        data,
        sql,
        id1,
        id2,
        cmd_tag,
        verbose):
    """Clean up the data after transformation"""
    # making functions more explicit
    data, sql, id1, id2, cmd_tag, verbose = \
        data, sql, id1, id2, cmd_tag, verbose
    if verbose >= 2:
        print("Data is being polished")
    data[sql].astype(str)
    data = data.loc[data[sql].str.contains('execute')]
    data['total_duration'].dropna().astype(float)
    data = data.drop_duplicates([id1, id2], keep='first')
    data = data.loc[(data[cmd_tag] == 'SELECT') | (data[cmd_tag] == 'INSERT') |
                    (data[cmd_tag] == 'BIND') | (data[cmd_tag] == 'PARSE')]
    if verbose >= 2:
        print("Data has been polished")
    return data
