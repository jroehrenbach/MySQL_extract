# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:14:06 2019

@author: jakob
"""



from wrapper import pymysql_wrapper
import json



def main():
    
    #> enter arguments for pymysql.connect...
    host = "47.95.243.17"
    user = "root"
    passwd = "Abc123456"
    db_name = "result"
    
    # wrapper object for pymysql (also connects to database)
    db = pymysql_wrapper(host, user, passwd, db_name)
    
    # loading queries
    queries = json.load(open("queries.json"))
    
    # extracting data from data base
    data = {}
    for name, query_dict in queries.items():
        data[name] = db.query(query_dict)
    
    #> do stuff with data...
    print(data)
    
    db._close()


if __name__ == "__main__":
    main()