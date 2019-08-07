import argparse


def parsargs():
    """Specify the user defined arguments"""
    parser = argparse.ArgumentParser(
        description="Methods to visualize and identify those who may join"+ \
            " the ranks of the einherjar in valhalla")

# -----> variables for core functionality of einherjar
    parser.add_argument(
        '-d',
        dest = 'datatype',
        type=str,
        choices=[
            'csv',
            'sqlite3',
            'postgres'],
        help='What form of data are you trying to access?')
    parser.add_argument(
        '-f',
        dest = 'fpath',
        type=str,
        help='File path to desired data')
    parser.add_argument(
        '-n',
        dest = 'column_names',
        type=str, 
        help='The names of the columns within your dataset')

# -----> define the columns that contain the most important data
    parser.add_argument(
        '--sql',
        dest = 'sql',
        type=str,
        help='Which column contians the sql script enacted upon the database?')
    parser.add_argument(
        '--dur',
        dest = 'duration',
        type=str,
        help='Which column details the latency of the query?')
    parser.add_argument(
        '--id1',
        dest = 'id1',
        type=str,
        help='Which column can be used as the first form of identification?')
    parser.add_argument(
        '--id2',
        dest = 'id2',
        type=str,
        help='Which column can be used as the second form of unique\
        indenification?')
    parser.add_argument(
        '--cmd',
        dest = 'cmd_tag',
        type=str,
        help='Which column in your data specifies the type of query enacted\
        on the database?')

# -----> export your data using matplotlib
    parser.add_argument(
        '--pt',
        dest = 'ftype_plots',
        type=str,
        choices=[
            'pdf',
            'html'],
        help='Specifity the filetype of the exported plots')

# -----> export raw data files
    parser.add_argument(
        '-t',
        '--et',
        dest = 'ftype_data',
        type=str,
        choices=[
            'xlsx',
            'csv'],
        help='In what file type would you like your raw data to be exported?')

# -----> export selected fastest / slowest queries
    parser.add_argument(
        '--nq',
        dest = 'n_queries',
        type=str,
        help='# of queries in each exported file')

# -----> define the ways to connect with a postgres database
    parser.add_argument(
        '-c',
        dest = 'connection',
        type=str,
        help='Define the ways to connect to your database')
    
    parser.add_argument(
        '--dc',
        dest = 'desired_columns',
        type = str,
        help = "Which column(s) would you like to access from the database?"
    )

    parser.add_argument(
        '--dt',
        dest = 'desired_table',
        type = str,
        help = "Which table would you like to access from the database?"
    )

# -----> allows the user to define how much feed back they would like to 
#        receive from the program
    parser.add_argument(
        '-v',
        dest = 'verbose',
        action = 'count', 
        help='On a scale of 0-3, how muh feedback would you like to recieve\
         from the program?')

# -----> allows the user to specify information for altair
    parser.add_argument(
        '-p',
        dest = 'parameters',
        type = str,
        help='Which column defines the parameters of said query?')

# -----> setting mutually exclusive groups
# built using this guide: https://stackoverflow.com/a/31347222
    # has_headers
    headers_parser = parser.add_mutually_exclusive_group(required = False)
    headers_parser.add_argument(
        '--headers',
        dest = 'has_headers',
        action = 'store_true',
        help = "Your data has headers")
    headers_parser.add_argument(
        '--no-headers',
        dest = 'has_headers',
        action = 'store_false',
        help = "Your data doesn't have headers")
    
	# plots
    plots_parser = parser.add_mutually_exclusive_group(required = False)
    plots_parser.add_argument(
        '--plots',
        dest = 'plots',
        action = 'store_true',
        help = "Use matplotlib to export your data")
    plots_parser.add_argument(
        '--no-plots',
        dest = 'plots',
        action = 'store_false',
        help = "Don't use matplotlib to exprrt your data")

	# exec_export
    export_parser = parser.add_mutually_exclusive_group(required = False)
    export_parser.add_argument(
        '--export',
        dest = 'exec_export',
        action = 'store_true',
        help = "Export the transformed data")
    export_parser.add_argument(
        '--no-export',
        dest = 'exec_export',
        action = 'store_false',
        help = "Don't export the transformed data")
    
	# skim_data
    skim_parser = parser.add_mutually_exclusive_group(required = False)
    skim_parser.add_argument(
        '--skim',
        dest = 'skim_data',
        action = 'store_true',
        help = "Export only a slice of the data")
    skim_parser.add_argument(
        '--no-skim',
        dest = 'skim_data',
        action = 'store_false',
        help = "Don't export a slice of the data")
    
	# fastest
    fast_parser = parser.add_mutually_exclusive_group(required = False)
    fast_parser.add_argument(
        '--fastest',
        dest = 'fastest',
        action = 'store_true',
        help = 'Exported the fastest queries')
    fast_parser.add_argument(
        '--no-fastest',
        dest = 'fastest',
        action = 'store_false',
        help = "Don't export the fastest queries")
    
	# slowest
    slow_parser = parser.add_mutually_exclusive_group(required = False)
    slow_parser.add_argument(
        '--slowest',
        dest = 'slowest',
        action = 'store_true',
        help = "Export the slowest queries")
    slow_parser.add_argument(
        '--no-slowest',
		dest = 'slowest',
		action = 'store_false',
		help = "Don't export the slowest queries")

    # exec_vega
    vega_parser = parser.add_mutually_exclusive_group(required = False)
    vega_parser.add_argument(
        '--vega',
        dest = 'exec_vega',
        action = 'store_true',
        help = "Export your data using vega graphics")
    vega_parser.add_argument(
        '--no-vega',
		dest = 'exec_vega',
        action = 'store_false',
        help = "Don't export your data using vega graphics")

    # system prompt
    volume = parser.add_mutually_exclusive_group(required = False)
    volume.add_argument(
        '--silent',
        dest = 'volume',
        action = 'store_true',
        help = "Don't have a user prompt")
    volume.add_argument(
        '--loud',\
        dest = 'volume',
        action = 'store_false',
        help = "Have a user prompt")
    
# ----->
    # set defaults for booleans
    parser.set_defaults(has_headers = False)
    parser.set_defaults(plots = True)
    parser.set_defaults(exec_export = True)
    parser.set_defaults(skim_data = True)
    parser.set_defaults(fastest = True)
    parser.set_defaults(slowest = True)
    parser.set_defaults(exec_vega = True)
    parser.set_defaults(volume = False)
    parser.set_defaults(machine_learning = False)

    # set defaults for everything else
    parser.set_defaults(verbose = 2)
    parser.set_defaults(datatype = "postgres")
    parser.set_defaults(fpath = "postgresql-Thu.csv")
    parser.set_defaults(verbose = 2)
    parser.set_defaults(column_names = "log_time_with_tz,username," \
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
    parser.set_defaults(cmd_tag = "command_tag")
    parser.set_defaults(parameters = "detail")
    parser.set_defaults(ftype_plots = "pdf")
    parser.set_defaults(ftype_data = "csv")
    parser.set_defaults(n_queries = 100)
    parser.set_defaults(test_string = "")
    parser.set_defaults(connection = \
        "host='postgres_log_pg_1' dbname='logging'" \
        +"user='postgres' password='valhalla'")
    parser.set_defaults(desired_columns = "*")
    parser.set_defaults(desired_table = "vw_query_duration")

# ----->
    # close parser
    args = parser.parse_args()
    return args
