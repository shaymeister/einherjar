import tfd_accessed_column as skylake 
import tfd_accessed_table as ryzen   
import tfd_inserted_data as haswell 
import tfd_polish_data as kabylake
import tfd_total_duration as broadwell  
import pandas


def transformData(
        data,
        sql,
        duration,
        id1,
        id2,
        cmd_tag,
        verbose):
    """Use other functions to extrcat desired data from database"""
    # making function more explicit
    data, sql, duration, id1, id2, cmd_tag, verbose = \
        data, sql, duration, id1, id2, cmd_tag, verbose

    if verbose >= 1:
        print("Transforming Data")

# -----> determine the total duration of each query
    data = broadwell.totalDuration(
                data,
                duration,
                id1,
                id2,
                verbose)

# -----> determine the accessed table in each query
    data = ryzen.accessedTable(
                data,
                sql,
                verbose)
    
# -----> determine the accessed column in each query
    data = skylake.accessedColumn(
                data,
                sql,
                verbose)

# -----> determine data inserted into the database
    data = haswell.insertedData(
                data,
                sql,
                id1,
                id2,
                cmd_tag,
                verbose)

# -----> polish the recently merged data
    data = kabylake.polishData(
                data,
                sql,
                id1,
                id2,
                cmd_tag,
                verbose)

    if verbose >= 1:
        print("Data has been transformed")
    return data
