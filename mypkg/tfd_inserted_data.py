#!/usr/bin/env python3
import pandas


def insertedData(
        data,
        sql,
        id1,
        id2,
        cmd_tag,
        verbose):
    """Extract the information that was inserted into the data"""
    # making function more explicit
    data, sql, id1, id2, cmd_tag, verbose = \
        data, sql, id1, id2, cmd_tag, verbose
    insert_data = data.copy()
    if verbose >= 2:
        print("Extracting the inserted data")
    insert_data = insert_data.loc[insert_data[cmd_tag] == 'INSERT']
    insert_data[sql] = insert_data[sql].astype(str)
    insert_data[sql] = insert_data[sql].str.extract(
        r'((:\s\S*)*)', expand=False).astype(str)
    insert_data[sql] = insert_data[sql].str.extract(
        r'((\S{2,})*)', expand=False)
    if verbose >= 2:
        print("Extracted the inserted data\nMerging with original dataset")
    insert_data_merge = insert_data[[id1, id2, sql]]
    data = pandas.merge(data, insert_data_merge, on=(id1, id2), how='outer')
    data = data.rename(columns={sql + '_x': sql, sql + '_y': 'inserted_data'})
    if verbose >= 2:
        print("The inserted data has been merged and renamed")
    return data
