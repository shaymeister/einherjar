#!/usr/bin/env python3
import pandas


def exportData(
        exportFastest,
        exportFileType,
        exportSlowest,
        numberOfQueries,
        skimData,
        transformedData,
        verbose):
    """Export the raw data to specified filetype"""

    # making function more explicit
    exportFastest = exportFastest
    exportFileType = exportFileType
    exportSlowest = exportSlowest
    numberOfQueries = numberOfQueries
    skimData = skimData
    transformedData = transformedData
    verbose = verbose

    # inform user of program progress
    if verbose >= 1:
        print(
            "Starting exportData()"
        )

    # create a copy of the original dataframe
    data = transformedData.copy()

    # inform user of program progress
    if verbose >= 2:
        print(
            "Exporting data to .csv"
        )

    # export the data frame to a .csv
    data.to_csv(
        "results/evolved_data.csv"
    )

    # inform user of program progress
    if verbose >= 2:
        print(
            "Data has been exported to .csv"
        )

    # sort dataframe by 'total_duration' column
    data = data.sort_values(
        by = ["total_duration"],
        ascending = False,
    )

# -----> Export only select parts of data
    if skimData:
        x = int(numberOfQueries)
        y = str(numberOfQueries)
    # -----> export exportSlowest queries
        if exportSlowest:
            
            # export dataframe to .xlsx
            if exportFileType == "xlsx":
                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " slowest queries are being exported"\
                          + " to .xlsx"
                    )

                # export top x exportSlowest queries to .xlsx
                data.head(x).to_excel(
                    "results/" + y + "_slowest_queries.xlsx"
                )

                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " slowest queries have been exported " \
                          + "to .xlsx"
                    )

            # export data to .csv
            else:
                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " slowest queries are being exported " \
                          + "to .csv"
                    )

                # export top x exportSlowest queries to .csv
                data.head(x).to_csv(
                    "results/" + y + "_exportSlowest_queries.csv"
                )

                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " slowest queries have been " \
                          + "exported to .csv"
                    )

    # -----> export exportFastest queries
        # used to get correct order in exported data

        # sort dataframe by 'total_duration'
        data_opp = data.sort_values(
            by = ["total_duration"],
            ascending = True,
        )

        if exportFastest:
            # export dataframe to .xlsx
            if exportFileType == "xlsx":

                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " fastest queries are being " \
                          + "exported to .xlsx"
                    )

                # export top x exportFastest queries to .xlsx
                data_opp.head(x).to_excel(
                    "results/" + y + "_fastest_queries.xlsx"
                )

                # inform use of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " fastest queries have been exported " \
                          + "to .xlsx"
                    )

            # export dataframe to .csv
            else:
                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " fastest queries are being exported " \
                          + "to .csv"
                    )

                # export top x exportFastest queries to .csv
                data_opp.head(x).to_csv(
                    "results/" + y + "_fastest_queries.csv"
                )

                # inform user of program progress
                if verbose >= 2:
                    print(
                        "The " + y + " fastest queries have been exported " \
                          + "to .csv"
                    )

    # inform user of program progress
    if verbose >= 1:
        print(
            "Data has been exported\n" \
              + "exportData() is complete"
        )