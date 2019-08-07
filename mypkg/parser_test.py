#!/usr/bin/env python3
import einherjar_parser
import sys



args = einherjar_parser
def parserTest(args, volume):
# --> checking datatype
    args, volume = \
        args, volume

# -----> csv
    if args.datatype == 'csv':
        print("USING DEFAULT: Importing data from " + args.datatype)
        if args.fpath == '/home/ses/einherjar/data/postgresql-Thu.csv':
            print("USING DEFAULT: fpath to your " + args.datatype + " file:" \
                 + " " + args.fpath)

        else:
            print("fpath to your " + args.datatype + " file: " + args.fpath)
        header_test = True

# -----> sqlite3
    elif args.datatype == 'sqlite3':
        if args.fpath == '/home/ses/einherjar/data/postgresql-Thu.csv':
            print("You must specify the path to you sqlite3 database")
            sys.exit()

        else:
            print("Connecting to " + args.datatype + " at " + args.fpath)
            header_test = True

# -----> postgres
    elif args.datatype == 'postgres':
        if args.connection == "host='postgres_log_pg_1' dbname='logging' " \
                + "user='postgres' password='valhalla'":
            print("USING DEFAULT: network parameters= " + args.connection)

        else:
            print("network parameters = " + args.connection)

        if args.desired_columns == "*":
            print("USING DEFAULT: Extracting from all columns")

        else:
            print("Extracting from column: " + args.desired_columns)

        if args.desired_table == "vw_query_duration":
            print("USING DEFAULT: Extracting data from table: vw_query_duration")

        else:
            print("Extracting from table: " + args.desired_table)

# -----> else
    else:
        print("Importing data from " + args.datatype)
        if args.fpath == '/home/ses/einherjar/data/postgresql-Thu.csv':
            print("DEFAULT: fpath to your data: " + args.fpath)

        else:
            print("fpath to your data: " + args.fpath)

# -----> headers
    if header_test == True:
        if args.has_headers == False:
            if args.column_names == "log_time_with_tz,username," \
                + "database_name,process_id,connection_from,session_id," \
                + "session_line_number,command_tag," \
                + "session_start_time_with_tz,virtual_transaction_id," \
                + "transaction_id,error_sensetivity,sql_state_code,latency," \
                + "detail,hint,internal_query,internal_query_position," \
                + "context,query,query_position,location,application_name":
                print("USING DEFAULT Column Headers: " + args.column_names)

            else:
                print("Column Headers: " + args.column_names)

        else:
            print("Assuming your data has pre-defined column headers")
# -----> specification of important columns
    # query details
    if args.sql == 'latency':
        print("USING DEFAULT: column " + args.sql + " has the query enacted" \
              + " upon the data")

    else:
        print("Column " + args.sql + " has the query enacted upon the data")

    # total duration of respective query
    if args.duration == 'latency':
        print("USING DEFAULT: column " + args.duration + " has the total " \
              + "duration of each query")

    else:
        print("Column " + args.duration + " has the total duration of each" \
              + " query")

    # unique identifiers
    if args.id1 == args.id2:
        print("WARNING: id1 and id2 much be unique")
        sys.exit()

    else:
        # 1st unique id
        if args.id1 == 'session_id':
            print("USING DEFAULT: The first unique identifier is " + args.id1)

        else:
            print("The first unique identifier is " + args.id1)

        # 2nd unique id
        if args.id2 == 'virtual_transaction_id':
            print("USING DEFAULT: The second unique identifier is " + \
                  args.id2)

        else:
            print("The second unique identifier is " + args.id2)

    # command tag
    if args.cmd_tag == 'command_tag':
        print("USING DEFAULT: The command tag is located with the " \
              + args.cmd_tag + " column")

    else:
        print("The command tag is located within the "+args.cmd_tag+" column")

# -----> matplotlib
    if args.plots == True:
        print("USING DEFAULT: Matplotlib will be utilized")
        if args.ftype_plots == 'pdf':
            print("USING DEFAULT: Plots will be exported to " + \
                  args.ftype_plots)

        else:
            print("Plots will be exported to " + args.ftype_plots)

    else:
        print("Matplotlib will not be utilized")

# -----> vega graphics
    if args.exec_vega == True:
        print("USING DEFAULT: Vega Graphics will be created")
        if args.parameters == 'detail':
            print("USING DEFAULT: The column " + args.parameters + \
                  " contains the parameters of the query")

        else:
            print("The column " + args.parameters + " contains the " + \
                  "parameters of the query")

    else:
        print("Vega Graphics won't be created")

# -----> export data
    if args.exec_export == True:
        print("USING DEFAULT: Your transformed data will be exported")
        if args.ftype_data == 'csv':
            print("USING DEFAULT: Your data will be in " + args.ftype_data + \
                  " format")

        elif args.ftype_data == 'xlsx':
            print("Your data will be in " + args.ftype_data + " format")

        if args.skim_data == True:
            print("USING DEFAULT: A slice of your data will be exported")
            if args.fastest == False and args.slowest == False:
                print("WARNING: You must request at least one: fastest" + \
                      " or slowest")
                skim = False
            else:
                skim = True

        else:
            print("A slice of your data will not be exported")
            skim = False

    else:
        print("Your transformed data won't be exported")
        skim = False

    if skim == True:
    # --> # of Queries
        if args.n_queries == 1000:
            print("USING DEFAULT: 1000 queries will be sliced")

        else:
            print(str(args.n_queries) + " queries will be sliced")

    # --> Fastest Queries
        if args.fastest == True:
            print(str(args.n_queries) + " of the fastest queries will " \
                  + "be exported")

        else:
            print("The fastest queries will not be exported")

    # --> Slowest Queries
        if args.slowest == True:
            print(str(args.n_queries) + " of the slowest queries will " \
                  + "be exported")
        else:
            print("The slowest queries will not be exported")

    corvette = input("Would you like to continue with these options? [y/n] ")
    if corvette == 'n':
        sys.exit()

    elif corvette == 'y':
        pass

    else:
        print("Incorrect character was entered")
        sys.exit()

    return
