#!/usr/bin/env python3
import pandas


def totalDuration(data, duration, id1, id2, verbose):
    """Extract the total duration of each query"""
    total_duration = data.copy()
    if verbose >= 2:
        print("Extracting total duration of each query")
    total_duration[duration] = total_duration[duration].str.extract(
        '(\d{1,}\.\d{1,}(?=\sms))').astype(float).dropna()
    total_duration[duration] = total_duration[duration].astype(float).dropna()
    true_sum_of_time = total_duration.groupby([id1, id2])[duration].sum()
    if verbose >= 2:
        print("Extracted total duration\nMerging with original dataset")
    data = pandas.merge(data, true_sum_of_time, on=(id1, id2), how='outer')
    data = data.rename(
        columns={
            duration +
            '_x': duration,
            duration +
            '_y': 'total_duration'})
    if verbose >= 2:
        print("Total Duration has been merged and renamed")
    return data
