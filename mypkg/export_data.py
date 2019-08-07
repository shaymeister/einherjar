#!/usr/bin/env python3
import pandas


def exportData(
        transformed_data,
        slowest,
        fastest,
        ftype_data,
        verbose,
        n_queries,
        skim_data):
    """Export the raw data to specified ftype"""
    # making function more explicit
    transformed_data, slowest, fastest, ftype_data, verbose, n_queries, skim_data = transformed_data, slowest, fastest, ftype_data, \
        verbose, n_queries, skim_data
    if verbose >= 1:
        print("Starting exportData()")
    data = transformed_data.copy()

    if verbose >= 2:
        print("Exporting data to .csv")
    data.to_csv('evolved_data.csv')
    if verbose >= 2:
        print("Data has been exported to .csv")

    data = data.sort_values(by=['total_duration'], ascending=False)

# -----> Export only select parts of data
    if skim_data == True:
        x = int(n_queries)
        y = str(n_queries)
    # -----> export slowest queries
        if slowest == True:
            if ftype_data == 'xlsx':
                if verbose >= 2:
                    print("The " + y + \
                        " slowest queries are being export t0.xlsx")
                data.head(x).to_excel(y + '_slowest_queries.xlsx')
                if verbose >= 2:
                    print("The " + y + \
                        " slowest queries have been exported to .xlsx")
            else:
                if verbose >= 2:
                    print("The " + y + \
                        " slowest queries are being exported to .csv")
                data.head(x).to_csv(y + '_slowest_queries.csv')
                if verbose >= 2:
                    print("The " + y + " slowest queries have been exported to .csv")

    # -----> export fastest queries
        # used to get correct order in exported data
        data_opp = data.sort_values(by=['total_duration'], ascending=True)
        if fastest == True:
            if ftype_data == 'xlsx':
                if verbose >= 2:
                    print( "The " + y + \
                        " fastest queries are being exported to .xlsx")
                data_opp.head(x).to_excel(y + "_fastest_queries.xlsx")
                if verbose >= 2:
                    print("The " + y + \
                        " fastest queries have been exported to .xlsx")

            else:
                if verbose >= 2:
                    print("The " + y + \
                        " fastest queries are being exported to .csv")
                data_opp.head(x).to_csv(y + "_fastest_queries.csv")
                if verbose >= 2:
                    print("The " + y + \
                        " fastest queries have been exported to .csv")

    if verbose >= 1:
        print("Data has been exported\nexportData() is complete")
