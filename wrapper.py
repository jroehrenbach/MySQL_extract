# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:43:01 2019

@author: jakob
"""

import pymysql
import pandas as pd


class pymysql_wrapper(object):
    """wrapper class for pymysql for extracting data"""
    
    def __init__(self, host, user, passwd, db_name):
        """
        Parameters
        ----------
        host : str
        user : str
        passwd : str
        db : str
        """
        
        self._host = host
        self._user = user
        self._passwd = passwd
        self._db_name = db_name
        self._connected = False
        self._open()
    
    
    def __del__(self):
        self._close()
    
        
    def _open(self):
        """
        Connects to data base
        
        Returns
        -------
        True if connection succeeded
        """
        
        try:
            self._connection = pymysql.connect(
                    host = self._host,
                    user = self._user,
                    passwd = self._passwd,
                    db = self._db_name
                    )
            self._cursor = self._connection.cursor()
            self._connected = True
            return True
        
        except Exception as e:
            print(e)
            raise IOError("could not connect to data base")
    
    
    def _close(self):
        """
        Disconnects from data base
        
        Returns
        -------
        True if disconnection succeeded
        """
        
        if not self._connected:
            return True
        
        try:
            self._cursor.close()
            self._connection.close()
            self._connected = False
            return True
        except:
            return False
    
    
    def _fetch(self, sql_string):
        """
        Extracts data from database using the cursor
        
        Parameters
        ----------
        sql_string : str
            sql code for fetching desired data
        
        Returns
        -------
        data : tuple
            tuple which contains desired data
        """
        
        if not self._connected:
            raise IOError("not connected to data base")
        
        try:
            self._cursor.execute(sql_string)
        except:
            raise IOError("could not execute sql_string >%s" % sql_string)
        
        try:
            data = self._cursor.fetchall()
        except:
            raise IOError("could not fetch data")
            
        # tuple to list
        data = [list(d) for d in data]
        return data
    
    
    def _get_sql_string(self, query_dict):
        """
        Creates sql_string from query_dict
        
        Parameters
        ----------
        query_dict : dict
            Contains instructions for creating sql_string
        
        Returns
        -------
        sql_string : str
            sql code for fetching desired data
        """
        
        # create sql string from query_dict
        sql_string = "select " + ",".join(query_dict["columns"])
        sql_string += " from " + query_dict["table"]
        
        if "rules" in query_dict:
            for rule, column in query_dict["rules"].items():
                sql_string += " " + rule % column
        
        return sql_string
    
    
    def query(self, query_dict):
        """
        Queries data from opened data base using the query_dict
        
        Parameters
        ----------
        query_dict : dict
            Contains instructions for creating sql_string
        
        Returns
        -------
        df : pd.DataFrame
            Data frame with desired data
        """
        
        sql_string = self._get_sql_string(query_dict)
        data = self._fetch(sql_string)
        df = pd.DataFrame(data, columns=query_dict["columns"])
        #> do some processing following instructions from query_dict
        return df