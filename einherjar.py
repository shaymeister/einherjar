#!/usr/bin/env python3
import einherjar_parser
import export_data
import import_data
import parser_test
import plot_data
import transform_data
import vega_graphics
import argparse
import sys


def main():
    """The core functionality of einherjar"""
    # defining args using argparse
    args = einherjar_parser.parsargs()

# -----> testing arguments
    if args.volume == False:
        parser_test.parserTest(
                        args,
                        args.verbose)

# -----> calling functions
    # calling importData()
    data = import_data.importData(
        args.column_names,
        args.connection,
        args.datatype,
        args.fpath,
        args.has_headers,
        args.desired_columns,
        args.desired_table,
        args.verbose)
    # calling transformData()
    transformed_data = transform_data.transformData(
        data,
        args.sql,
        args.duration,
        args.id1,
        args.id2,
        args.cmd_tag,
        args.verbose)
    if args.verbose >= 1:
        print("The core functionality of einherjar is completed\nStarting optional functionality")

# -----> here: the user has the option to visualize their data using vega graphics
    if args.exec_vega == True:
        vega_graphics.vegaGraphics(
            transformed_data,
            args.verbose,
            args.cmd_tag,
            args.sql,
            args.id1,
            args.id2,
            args.parameters)

# -----> here: the user has the option to visualize their data using matplotlib
    if args.plots == True:
        plot_data.plotData(
            transformed_data,
            args.ftype_plots,
            args.verbose)

# -----> here: the user has the option to export the recently maniplated data
    if args.exec_export == True:
        export_data.exportData(
            transformed_data,
            args.slowest,
            args.fastest,
            args.ftype_data,
            args.verbose,
            args.n_queries,
            args.skim_data)

    if args.verbose >= 1:
        print("optional funcations have been completed\nEinherjar is 100% COMPLETE")


if __name__ == '__main__':
    main()
