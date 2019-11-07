import pandas

from valkyrie_pkg import tfd_accessed_column
from valkyrie_pkg import tfd_accessed_table 
from valkyrie_pkg import tfd_inserted_data
from valkyrie_pkg import tfd_polish_data
from valkyrie_pkg import tfd_total_duration


def transformData(
        cmdTag,
        data,
        duration,
        id1,
        id2,
        sql,
        verbose):
    """Use other functions to extrcat desired data from database"""
    # making function more explicit
    cmdTag = cmdTag
    data = data
    duration = duration
    id1 = id1
    id2 = id2
    sql = sql
    verbose = verbose

    # inform user of program progress
    if verbose >= 1:
        print(
            "Transforming Data"
        )

# -----> determine the total duration of each query
    data = tfd_total_duration.totalDuration(
                data,
                duration,
                id1,
                id2,
                verbose
    )

# -----> determine the accessed table in each query
    data = tfd_accessed_table.accessedTable(
                data,
                sql,
                verbose
    )
    
# -----> determine the accessed column in each query
    data = tfd_accessed_column.accessedColumn(
                data,
                sql,
                verbose
    )

# -----> determine data inserted into the database
    data = tfd_inserted_data.insertedData(
                cmdTag,
                data, 
                id1,
                id2,
                sql,
                verbose
    )

# -----> polish the recently merged data
    data = tfd_polish_data.polishData(
                cmdTag,
                data,     
                id1,
                id2,
                sql,
                verbose
    )

    # inform user of program progress
    if verbose >= 1:
        print(
            "Data has been transformed"
        )

    # return dataframe to runtime environment
    return data