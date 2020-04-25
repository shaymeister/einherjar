import argparse


def parsargs():
    """Specify the user defined arguments"""
    parser = argparse.ArgumentParser(
        description = 
            "Methods to visualize and identify those who may join " \
              + "the ranks of the einherjar in valhalla"
    )

# -----> variables for core functionality of einherjar
    parser.add_argument(
        "-d",
        dest = "importDataType",
        type = str,
        choices = [
            "csv",
            "sqlite3",
            "postgres"],
        help = "What form of data are you trying to access?",
    )
    parser.add_argument(
        "-f",
        dest = "filePath",
        type = str,
        help = "file path to desired data",
    )
    parser.add_argument(
        "-n",
        dest = "columnNames",
        type = str, 
        help = "The names of the columns within your dataset",
    )

# -----> define the columns that contain the most important data
    parser.add_argument(
        "--sql",
        dest = "sql",
        type = str,
        help = "Which column contains the sql script?",
    )
    parser.add_argument(
        "--dur",
        dest = "duration",
        type = str,
        help = "Which column details the latency of the query?",
    )
    parser.add_argument(
        "--id1",
        dest = "id1",
        type = str,
        help = "Which column can be used as the first form of identification?",
    )
    parser.add_argument(
        "--id2",
        dest = "id2",
        type = str,
        help = "Which column can be used as second unique identification?",
    )
    parser.add_argument(
        "--cmd",
        dest = "cmdTag",
        type = str,
        help = "Which column specifies the type of query enacted?",
    )

# -----> export your data using matplotlib
    parser.add_argument(
        "--pt",
        dest = "fileTypePlots",
        type = str,
        choices = [
            "pdf",
            "html"],
        help = "Specify the filetype of the exported plots",
    )

# -----> export raw data files
    parser.add_argument(
        "-t",
        "--et",
        dest = "exportFileType",
        type = str,
        choices = [
            "xlsx",
            "csv"],
        help = "In what file type would you like your raw data to be exported?",
    )

# -----> export selected fastest / slowest queries
    parser.add_argument(
        "--nq",
        dest = "numberOfQueries",
        type = str,
        help = "# of queries in each exported file",
    )

# -----> define the ways to connect with a postgres database
    parser.add_argument(
        "-c",
        dest = "connection",
        type = str,
        help = "Define the ways to connect to your database",
    )
    
    parser.add_argument(
        "--dc",
        dest = "desiredColumns",
        type = str,
        help = "Which column(s) would you like to access from the database?",
    )

    parser.add_argument(
        "--dt",
        dest = "desiredTable",
        type = str,
        help = "Which table would you like to access from the database?",
    )

# -----> allows the user to define how much feed back they would like to 
#        receive from the program
    parser.add_argument(
        "-v",
        dest = "verbose",
        action = "count", 
        help = "On a scale of 0-3, how much feedback would you like?",
    )

# -----> allows the user to specify information for altair
    parser.add_argument(
        "-p",
        dest = "parameters",
        type = str,
        help="Which column defines the parameters of said query?",
    )

# -----> setting mutually exclusive groups
# built using this guide: https://stackoverflow.com/a/31347222
    # does the data being imported have predefined column headers
    headersParser = parser.add_mutually_exclusive_group(required = False)
    headersParser.add_argument(
        "--headers",
        dest = "hasHeaders",
        action = "store_true",
        help = "Your data has headers",
    )
    headersParser.add_argument(
        "--no-headers",
        dest = "hasHeaders",
        action = "store_false",
        help = "Your data doesn't have headers",
    )
    
	# would the user like to use matplotlib for visualization
    plotsParser = parser.add_mutually_exclusive_group(required = False)
    plotsParser.add_argument(
        "--plots",
        dest = "createPlots",
        action = "store_true",
        help = "Use matplotlib to export your data",
    )
    plotsParser.add_argument(
        "--no-plots",
        dest = "createPlots",
        action = "store_false",
        help = "Don't use matplotlib to export your data",
    )

	# would the user like to export the raw data
    exportParser = parser.add_mutually_exclusive_group(required = False)
    exportParser.add_argument(
        "--export",
        dest = "execExport",
        action = "store_true",
        help = "Export the transformed data",
    )
    exportParser.add_argument(
        "--no-export",
        dest = "execExport",
        action = "store_false",
        help = "Don't export the transformed data",
    )
    
	# would the user like to export a slice of the data
    skimParser = parser.add_mutually_exclusive_group(required = False)
    skimParser.add_argument(
        "--skim",
        dest = "skimData",
        action = "store_true",
        help = "Export only a slice of the data",
    )
    skimParser.add_argument(
        "--no-skim",
        dest = "skimData",
        action = "store_false",
        help = "Don't export a slice of the data",
    )
    
	# would the user like to export x number of the fastest queries
    fastParser = parser.add_mutually_exclusive_group(required = False)
    fastParser.add_argument(
        "--fastest",
        dest = "exportFastest",
        action = "store_true",
        help = "Exported the fastest queries",
    )
    fastParser.add_argument(
        "--no-fastest",
        dest = "exportFastest",
        action = "store_false",
        help = "Don't export the fastest queries",
    )
    
	# would the user like to export x number of the slowest queries
    slowParser = parser.add_mutually_exclusive_group(required = False)
    slowParser.add_argument(
        "--slowest",
        dest = "exportSlowest",
        action = "store_true",
        help = "Export the slowest queries",
    )
    slowParser.add_argument(
        "--no-slowest",
		dest = "exportSlowest",
		action = "store_false",
		help = "Don't export the slowest queries",
    )

    # would the user like to visualize their data using altair
    vegaParser = parser.add_mutually_exclusive_group(required = False)
    vegaParser.add_argument(
        "--vega",
        dest = "vegaGraphics",
        action = "store_true",
        help = "Export your data using vega graphics",
    )
    vegaParser.add_argument(
        "--no-vega",
		dest = "vegaGraphics",
        action = "store_false",
        help = "Don't export your data using vega graphics",
    )

    # would the user like the program to prompt them 
    volume = parser.add_mutually_exclusive_group(required = False)
    volume.add_argument(
        "--silent",
        dest = "volume",
        action = "store_true",
        help = "Don't have a user prompt",
    )
    volume.add_argument(
        "--loud",
        dest = "volume",
        action = "store_false",
        help = "Have a user prompt",
    )
    
# ---------------------------------------------------------------------
# Defaults for Parser
# ---------------------------------------------------------------------
    # set defaults for booleans
    parser.set_defaults(hasHeaders = False)
    parser.set_defaults(createPlots = True)
    parser.set_defaults(execExport = True)
    parser.set_defaults(skimData = True)
    parser.set_defaults(exportFastest = True)
    parser.set_defaults(exportSlowest = True)
    parser.set_defaults(vegaGraphics = True)
    parser.set_defaults(volume = False)

    # set defaults for everything else
    parser.set_defaults(verbose = 2)
    parser.set_defaults(importDataType = "csv")
    parser.set_defaults(filePath = "data/postgresql-Thu.csv")
    parser.set_defaults(columnNames = "log_time_with_tz,username," \
            +"database_name,process_id,connection_from,session_id," \
            +"session_line_number,command_tag,session_start_time_with_tz," \
            +"virtual_transaction_id,transaction_id,error_severity," \
            +"sql_state_code,latency,detail,hint,internal_query," \
            +"internal_qeary_position,context,query,query position," \
            +"location,application_name")
    parser.set_defaults(sql = "latency")
    parser.set_defaults(duration = "latency")
    parser.set_defaults(id1 = "session_id")
    parser.set_defaults(id2 = "virtual_transaction_id")
    parser.set_defaults(cmdTag = "command_tag")
    parser.set_defaults(parameters = "detail")
    parser.set_defaults(fileTypePlots = "pdf")
    parser.set_defaults(exportFileType = "csv")
    parser.set_defaults(numberOfQueries = 100)
    parser.set_defaults(connection = \
        "host="" dbname="" " \
        + "user="" password="""
    )
    parser.set_defaults(desiredColumns = "")
    parser.set_defaults(desiredTable = "")

# ----->
    # close parser
    args = parser.parse_args()
    return args