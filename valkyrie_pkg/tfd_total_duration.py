#!/usr/bin/env python3
import pandas


def totalDuration(
            data,
            duration,
            id1,
            id2,
            verbose):
    """Extract the total duration of each query"""
    # making functions more explicit
    data = data
    duration = duration
    id1 = id1
    id2 = id2
    verbose = verbose
    
    totalDuration = data.copy()

    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracting total duration of each query"
        )

    # extract the total duration of each query
    totalDuration[duration] = totalDuration[duration].str.extract(
        "(\d{1,}\.\d{1,}(?=\sms))").astype(float).dropna()
    totalDuration[duration] = totalDuration[duration].astype(float).dropna()
    trueSumOfTime = totalDuration.groupby([id1, id2])[duration].sum()

    # inform user of program progress
    if verbose >= 2:
        print(
            "Extracted total duration\n" \
              + "Merging with original dataset"
        )

    data = pandas.merge(
                    data,
                    trueSumOfTime,
                    on = (id1, id2),
                    how = "outer",
    )
    data = data.rename(columns={duration + "_x": duration,
                                duration + "_y": "total_duration"})

    # inform user of program progress
    if verbose >= 2:
        print(
            "Total Duration has been merged and renamed"
    )

    # return dataframe to runtime environment
    return data