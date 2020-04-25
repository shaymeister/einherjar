#!/usr/bin/env python3
import argparse 
import sys

from valkyrie_pkg import einherjar_parser
from valkyrie_pkg import export_data
from valkyrie_pkg import import_data
from valkyrie_pkg import parser_test
from valkyrie_pkg import plot_data
from valkyrie_pkg import transform_data
from valkyrie_pkg import vega_graphics



def main():
    """The core functionality of einherjar"""

    # einherjar_parser is a custom parser created specifically for
    # this program. Using argparse, this script was created to
    # define and manage the necessary variables for einherjar
    # to function properly. 
    args = einherjar_parser.parsargs()

    # By default, args.volume will be set to true. This enables
    # einherjar to take the variables from the parser and present
    # the information in a presentable display, informing the user
    # of the specifications by which this program will execute.
    # args.volume can be toggled to false by using the correct flag.
    if not args.volume:
        parser_test.parserTest(
            args,
            args.verbose,
        )

    # Here: the variables from einherjar_parser are being explicitly
    # defined. This was done to increase the explicitly of the program
    # A detailed explanation of these variable can be found within the
    # parser itself. There, the variable's abilities and description
    # are outlined.
    cmdTag = args.cmdTag
    columnNames = args.columnNames
    connection = args.connection
    createPlots = args.createPlots
    desiredColumns = args.desiredColumns
    desiredTable = args.desiredTable
    duration = args.duration
    execExport = args.execExport
    exportFastest = args.exportFastest
    exportFileType = args.exportFileType
    exportSlowest = args.exportSlowest
    filePath = args.filePath
    fileTypePlots = args.fileTypePlots
    hasHeaders = args.hasHeaders
    id1 = args.id1
    id2 = args.id2
    importDataType = args.importDataType
    numberOfQueries = args.numberOfQueries
    parameters = args.parameters
    skimData = args.skimData
    sql = args.sql
    vegaGraphics = args.vegaGraphics
    verbose = args.verbose
    volume = args.volume


    # Calling importData() which is located within the valkyrie_pkg
    # This function will import data from a variety of sources.
    # Said source will be determined given the user's arguments
    # The user's data will be returned as a dataframe and assigned
    # to the data variable. This variable will be used to move the 
    # dataframe throughout the rest of the program
    data = import_data.importData(
        columnNames,
        connection,
        desiredColumns,
        desiredTable,
        filePath,
        hasHeaders,
        importDataType,
        verbose,
    )

    # Calling transformData() which is located within the valkyrie_pkg
    # This function will take the aforementioned dataframe and extract
    # the necessary data. This "transformed" data will be assigned to
    # the transformedData variable
    transformedData = transform_data.transformData(
        cmdTag,
        data, 
        duration,
        id1,
        id2,
        sql,
        verbose,
    )

    # inform user of program progress
    if verbose >= 1:
        print(
            "The core functionality of einherjar is completed\n"
          + "Starting optional functionality"
        )

    # the user has the option to visualize 
    # their data using vega graphics
    if vegaGraphics:
        vega_graphics.vegaGraphics(
            cmdTag,
            id1,
            id2,
            parameters,
            sql,
            transformedData,
            verbose,
        )

    # The user has the option to visualize their data using matplotlib
    # If the user decided to use this functionality, their data will be
    # visualized in the plotData() function within valkyrie_pkg
    if createPlots:
        plot_data.plotData(
            fileTypePlots,
            transformedData,
            verbose,
        )

    # Here, the user has the option to export the manipulated data into
    # its raw format; they also have the ability to export x number of
    # the fastest and/or slowest queries from their database.
    if execExport:
        export_data.exportData(
            exportFastest,
            exportFileType,
            exportSlowest,
            numberOfQueries,
            skimData,
            transformedData,
            verbose,
        )

    # inform user of program completion
    if verbose >= 1:
        print(
            "Optional functions have been completed\n" 
              + "Einherjar is 100% COMPLETE"
        )

# This if statement checks if the script is executed by itself
# If so, the main method will be called.
if __name__ == "__main__":
    main()