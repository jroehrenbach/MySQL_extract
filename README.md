# MySQL_extract
Extract data from a MySQL data base using dicts as queries.
The dicts for querying the desired data are stored in queries.json and can be adapted easily (see below: queries.json).


### wrapper.py
This script contains wrapper class pymysql_wrapper.


### main.py
This script is for running pymysql_wrapper. Use this file for playing with the data.


### queries.json
Contains all queries which can be loaded and used on pymysql_wrapper.query
query_dict1 is an example for the query_dict which will be passed when calling pymysql.query


### members of query_dict: (as in queries.json)

#### "columns":
list of column names which should be extracted

#### "table":
Name of table which data should be extracted from

#### "rules": (optional)
dict of further operations like sorting or skimming
