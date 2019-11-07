#!/usr/bin/env python3
import pandas


def insertedData(
        cmdTag,
        data,
        id1,
        id2,
        sql,
        verbose):
    """Extract the information that was inserted into the data"""
    # making function more explicit
    cmdTag = cmdTag
    data = data
    id1 = id1
    id2 = id2
    sql = sql
    verbose = verbose
    
    insertData = data.copy()

    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracting the inserted data"
        )

    # determine the data inserted into the table
    insertData = insertData.loc[insertData[cmdTag] == "INSERT"]
    insertData[sql] = insertData[sql].astype(str)
    insertData[sql] = insertData[sql].str.extract(
                                    r'((:\s\S*)*)', expand = False).astype(str)
    insertData[sql] = insertData[sql].str.extract(
                                    r'((\S{2,})*)', expand = False)

    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracted the inserted data\n" \
              + "Merging with original dataset"
        )

    insertDataMerge = insertData[[id1, id2, sql]]
    data = pandas.merge(
                    data, 
                    insertDataMerge,
                    on = (id1, id2),
                    how = "outer",
    )
    data = data.rename(columns = {sql + "_x": sql, sql + "_y": "inserted_data"})

    # inform user of program progress
    if verbose >= 2:
        print(
            "The inserted data has been merged and renamed"
        )

    # return dataframe to runtime environment
    return data