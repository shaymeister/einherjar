#!/usr/bin/env python3
import sys

from valkyrie_pkg import einherjar_parser


def parserTest(einherjar_parser, volume):

# -----> defining variables from the parser
    args = einherjar_parser

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

# -----> checking all variables from parser <--------------------------

# --> checking importDataType
# -----> csv
    if importDataType == "csv":
        print("USING DEFAULT: Importing data from " + importDataType)
        if filePath == "/home/ses/einherjar/data/postgresql-Thu.csv":
            print(
                "USING DEFAULT: filePath to your " + importDataType + " file: " 
                + filePath
            )

        else:
            print(
                "File path to your " + importDataType + " file: " + filePath
            )

        headerTest = True

# -----> sqlite3
    elif importDataType == "sqlite3":
        if filePath == "/data/postgresql-Thu.csv":
            print(
                "You must specify the path to you sqlite3 database"
            )
            sys.exit()

        else:
            print(
                "Connecting to " + importDataType + " at " + filePath
            )
            headerTest = True

# -----> postgres
    elif importDataType == "postgres":
        if connection == "host='' dbname=' 'user='' password=''":
            print(
                "USING DEFAULT: network parameters= " + connection
            )

        else:
            print(
                "network parameters = " + connection
            )

        if desiredColumns == "":
            print(
                "USING DEFAULT: Extracting from zero columns"
            )

        else:
            print(
                "Extracting from column: " + desiredColumns
            )

        if desiredTable == "":
            print(
                "USING DEFAULT: Extracting data from table: none"
            )

        else:
            print(
                "Extracting from table: " + desiredTable
            )

# -----> else
    else:
        print(
            "Importing data from " + importDataType
        )
        if filePath == "/data/postgresql-Thu.csv":
            print(
                "DEFAULT: filePath to your data: " + filePath
            )

        else:
            print(
                "filePath to your data: " + filePath
            )

# -----> headers
    if not hasHeaders:
        if columnNames == "log_time_with_tz,username," \
            + "database_name,process_id,connection_from,session_id," \
            + "session_line_number,command_tag," \
            + "session_start_time_with_tz,virtual_transaction_id," \
            + "transaction_id,error_sensitivity,sql_state_code,latency," \
            + "detail,hint,internal_query,internal_query_position," \
            + "context,query,query_position,location,application_name":
            print(
                "USING DEFAULT Column Headers: " + columnNames
            )

        else:
            print(
                "Column Headers: " + columnNames
            )

    else:
        print(
            "Assuming your data has pre-defined column headers"
        )
# -----> specification of important columns
    # query details
    if sql == "latency":
        print(
            "USING DEFAULT: column " + sql + " has the query enacted " \
              + "upon the data"
        )

    else:
        print(
            "Column " + sql + " has the query enacted upon the data"
            )

    # total duration of respective query
    if duration == "latency":
        print(
            "USING DEFAULT: column " + duration + " has the total " \
              + "duration of each query"
        )

    else:
        print(
            "Column " + duration + " has the total duration of each" \
              + " query"
        )

    # unique identifiers
    if id1 == id2:
        print(
            "WARNING: id1 and id2 much be unique"
        )
        sys.exit()

    else:
        # 1st unique id
        if id1 == "session_id":
            print(
                "USING DEFAULT: The first unique identifier is " + id1
            )

        else:
            print(
                "The first unique identifier is " + id1
            )

        # 2nd unique id
        if id2 == "virtual_transaction_id":
            print(
                "USING DEFAULT: The second unique identifier is " + id2
            )

        else:
            print(
                "The second unique identifier is " + id2
            )

    # command tag
    if cmdTag == "command_tag":
        print(
            "USING DEFAULT: The command tag is located with the " \
              + cmdTag + " column"
        )

    else:
        print(
            "The command tag is located within the "+ cmdTag +" column"
        )

# -----> matplotlib
    if createPlots:
        print(
            "USING DEFAULT: Matplotlib will be utilized"
        )
        if fileTypePlots == "pdf":
            print(
                "USING DEFAULT: Plots will be exported to " \
                  + fileTypePlots
            )

        else:
            print(
                "Plots will be exported to " + fileTypePlots
            )

    else:
        print(
            "Matplotlib will not be utilized"
        )

# -----> vega graphics
    if vegaGraphics:
        print(
            "USING DEFAULT: Vega Graphics will be created"
        )
        if parameters == "detail":
            print(
                "USING DEFAULT: The column " + parameters \
                  + " contains the parameters of the query"
            )

        else:
            print(
                "The column " + parameters + " contains the " \
                  + "parameters of the query"
            )    

    else:
        print(
            "Vega Graphics won't be created"
        )

# -----> export data
    if execExport:
        print(
            "USING DEFAULT: Your transformed data will be exported"
        )
        if exportFileType == "csv":
            print(
                "USING DEFAULT: Your data will be in " + exportFileType \
                  + " format"
            )

        elif exportFileType == 'xlsx':
            print(
                "Your data will be in " + exportFileType + " format"
            )

        if skimData:
            print(
                "USING DEFAULT: A slice of your data will be exported"
            )
            if not exportFastest and not exportSlowest:
                print(
                    "WARNING: You must request at least one: exportFastest" \
                      + " or exportSlowest"
                )
                skim = False
            else:
                skim = True

        else:
            print(
                "A slice of your data will not be exported"
            )
            skim = False

    else:
        print(
            "Your transformed data won't be exported"
        )
        skim = False

    if skim:
    # --> # of Queries
        if numberOfQueries == 1000:
            print(
                "USING DEFAULT: 1000 queries will be sliced"
            )

        else:
            print(
                str(numberOfQueries) + " queries will be sliced"
            )

    # --> exportFastest Queries
        if exportFastest:
            print(
                str(numberOfQueries) + " of the exportFastest queries will " \
                  + "be exported"
            )

        else:
            print(
                "The exportFastest queries will not be exported"
            )

    # --> exportSlowest Queries
        if exportSlowest:
            print(
                str(numberOfQueries) + " of the exportSlowest queries will " \
                  + "be exported"
            )
        else:
            print(
                "The exportSlowest queries will not be exported"
            )

# determine if the user would like to execute
# w/ these program with these parameters
    resume = input(
        "Would you like to continue with these options? [y/n] "
    )
    if resume == "n":
        sys.exit()

    elif resume == "y":
        pass

    else:
        print(
            "Incorrect character was entered"
        )
        sys.exit()

# return to the runtime environment
    return