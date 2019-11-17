# Introduction
Einherjar, much like those chosen to die by the Valkyrie in Norse Mythology, is the query informatics tool associated with the VALKYRIE project. The purpose of this 
project is to choose those queries which are suboptimal so they may join the ranks of the Einherjar in Valhalla (and not be queried on the db anymore).
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Einherjar is a fairly complex program that utilizes a plethora of user defined / default arguments in order to make the program run correctly.
Using argparse, the user can use the '-h' flag to have the various arguments specified and explained here in the kernel.
Currently, Einherjar is able to extract data from three specific data sources: .csv, .db, and postgres.

# Visuals
The dialog box loacted in the image is a unique feature of Einherjar. When the user places their cursor over a given point, 
Einherjar will display the details of the query within a dialog box.
![Vega Graphics](/images/altair.png?raw=true "Queries")

# Installation
Einherjar is currently tested on the Windows Subsystem for Linux(UBUNTU), and Red Hat
To install from a fresh linux terminal:
``` 
    sudo apt update
    sudo apt install -y python3-pip
    sudo apt update python3-pip
    pip3 install pandas
    pip3 install matplotlib
    pip3 install numpy
    pip3 install scipy
    pip3 install argparse
    pip3 install altair
    pip3 install selenium
    pip3 install psycopg2-binary
```

Now you can run einherjar using "python3 einherjar <-options>" or "./einherjar.py <-options>"

# Usage
YOU MUST DECOMPRESS THE FILE WITHIN THE DATA DIRECTORY
The program will automatically default to importing data from the postgresql-Thu.csv file 
-The program also required the specification of the columns that contain the various data types
  One that contains the query enacted upon the database
  One that holds the duration of said query
  One that is a unique identifer to that specific query
  Another unique identifier to that specific query
  One that contains the command tag of said query
  Finally, one that contains the parameters for said query
^--The user can find the flags to specify each coloumn with the '-h' flag
```
usage: einherjar.py [-h] [-d {csv,sqlite3,postgres}] [-f FPATH]
                    [-z COLUMN_NAMES] [--sql SQL] [--dur DURATION] [--id1 ID1]
                    [--id2 ID2] [--cmd CMD_TAG] [--pt {pdf,html}]
                    [-t {xlsx,csv}] [-n N_QUERIES] [-c CONNECTION]
                    [--dc DESIRED_COLUMNS] [--dt DESIRED_TABLE] [-v]
                    [-p PARAMETERS] [--headers | --no-headers]
                    [--plots | --no-plots] [--export | --no-export]
                    [--skim | --no-skim] [--fastest | --no-fastest]
                    [--slowest | --no-slowest] [--vega | --no-vega]
                    [--silent | --loud]

Methods to visualize and identify those who may join the ranks of the einherjar
in valhalla

optional arguments:
  -h, --help            show this help message and exit
  -d {csv,sqlite3,postgres}
                        What form of data are you trying to access?
  -f FPATH              File path to desired data
  -z COLUMN_NAMES, --column_names COLUMN_NAMES
                        The names of the columns within your dataset
  --sql SQL             Which column contians the sql script enacted upon the
                        database?
  --dur DURATION        Which column details the latency of the query?
  --id1 ID1             Which column can be used as the first form of
                        identification?
  --id2 ID2             Which column can be used as the second form of unique
                        indenification?
  --cmd CMD_TAG         Which column in your data specifies the type of query
                        enacted on the database?
  --pt {pdf,html}       Specifity the filetype of the exported plots
  -t {xlsx,csv}
                        In what file type would you like your raw data to be
                        exported?
  -n N_QUERIES
                        # of queries in each exported file
  -c CONNECTION         Define the ways to connect to your database
  --dc DESIRED_COLUMNS  Which column(s) would you like to access from the
                        database?
  --dt DESIRED_TABLE    Which table would you like to access from the
                        database?
  -v                    On a scale of 0-3, how muh feedback would you like to
                        recieve from the program?
  -p PARAMETERS         Which column defines the parameters of said query?
  --headers             Your data has headers
  --no-headers          Your data doesn't have headers
  --plots               Use matplotlib to export your data
  --no-plots            Don't use matplotlib to exprrt your data
  --export              Export the transformed data
  --no-export           Don't export the transformed data
  --skim                Export only a slice of the data
  --no-skim             Don't export a slice of the data
  --fastest             Exported the fastest queries
  --no-fastest          Don't export the fastest queries
  --slowest             Export the slowest queries
  --no-slowest          Don't export the slowest queries
  --vega                Export your data using vega graphics
  --no-vega             Don't export your data using vega graphics
  --silent              Don't have a user prompt
  --loud                Have a user prompt
```        
If the user is wanting to use matplotlib, they have another argument they can specify
-by default, the plots will export to a pdf file
-with the '-e' flag the user can specify the report to be in html format aswell

If the user would like to use the exportData function, they more arguments they can specify
-by default, the program will export the the entirely new csv file with two more csv files,
  one of which contains the 100 fastest queries and the other containing the 100 slowest.
-the user has the option to change the number of queries export
 the option to choose whether the fastest and slowest files are exported
 the option to chose the file format for the exported file: csv or xlsx

If the user would like to access a postgres database, the last major argument is the connection argument
-using the "-c" flag, the user will create a string with the means of connecting to a postgres database 
Link to Altair documentation: https://altair-viz.github.io
Link to Matplotlib documentation: https://matplotlib.org

# Docker
To utilize docker, use the following commands along with decompressing the .csv within the data directory:
```
$ docker build -t einherjar .
$ docker run -it einherjar
$ docker cp <container id>:results <path/to/results/directory>
```

# Support 
For future support, users can contact me via my github handle "shaymeister" or email shaymeister@hotmail.com

# License
MIT

# Roadmap
Einherjar has many features that are currently being developed.
Such as: the ability to connect to a wider variety of databases a dashboard build using Flask,machine learning to predict a user defined query, and much much more!

# Authors and acknowldegment
Einherjar was created in the summer of 2019 at Oak Ridge National Laboratory with a partnership from the Oak Ridge Insitute for Science and Education                
Authored by: Shay Snyder                            
Major Contributors: Joshua Grant (ORNL), Bryan Eaton (ORNL), and Jesse Piburn (ORNL)                    
Acknowledgements: Dalton Lunga Ph.D (ORNL), Budhendra Bhaduri Ph.D (ORNL), Mary Sue Kelly-Cagle (ORISE), Loftin Gerberding (ORISE), Gabby Valentine (Niswonger Foundation), John Davison (NESCC), etc.                

# Project Status
Einherjar is still in development