#!/usr/bin/env python3
import pandas


def accessedColumn(
        data,
        sql,
        verbose):
    """Extract the accessed column from the specified data"""
    # making function more explicit
    data, sql, verbose = \
        data, sql, verbose
    if verbose >= 2:
        print("Extracting the accessed column")
    data['accessed_column'] = data[sql].astype(str).str.lower()
    data['accessed_column'] = data['accessed_column'].str.extract(r'(select\s\S*)')
    data['accessed_column'] = data['accessed_column'].str.extract(r'(\s\S*)')
    if verbose >= 2:
        print("Extracted the accessed column")

    return data
