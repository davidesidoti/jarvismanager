#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymysql import connect, cursors


class DBManager:
    config = {
        "host": "localhost", "user": "root", "password": "", "db": "test_jarvismanager", "cursorclass": cursors.DictCursor
    }

    def __init__(self) -> None:
        pass

    def connect(self):
        """
        The function attempts to establish a connection to a MySQL database using the provided
        credentials and returns a dictionary containing a cursor and connection object.
        :return: The connect() function is returning a dictionary with two keys: "cursor" and "conn".
        The value associated with the "cursor" key is the result of calling the create_cursor() method
        with the conn object as an argument. The value associated with the "conn" key is the conn object
        itself.
        """
        try:
            conn = connect(
                host='localhost',
                user='root',
                password='',
                db='test_jarvismanager',
                # Optional, for returning results as dictionaries
                cursorclass=cursors.DictCursor
            )
            return {"cursor": self.create_cursor(conn), "conn": conn}
        except Exception as e:
            raise e

    def create_cursor(self, conn):
        """
        The function creates a cursor object for a given connection.

        :param conn: The `conn` parameter is a connection object that represents a connection to a
        database. It is used to establish a connection to the database and perform various operations
        such as executing SQL queries and managing transactions
        :return: a cursor object.
        """
        return conn.cursor()

    def query(self, query: str, cursor=None):
        """
        The function executes a SQL query using a cursor and returns the fetched rows.
        
        :param query: The `query` parameter is a string that represents the SQL query you want to
        execute on the database. It can be any valid SQL statement, such as SELECT, INSERT, UPDATE,
        DELETE, etc
        :type query: str
        :param cursor: The `cursor` parameter is an optional parameter that represents the database
        cursor object. It is used to execute SQL queries and fetch the results from the database
        :return: the rows fetched from the database after executing the given query.
        """
        db = None
        if not cursor:
            db = self.connect()
            cursor = db["cursor"]

        cursor.execute(query)
        rows = cursor.fetchall()
        self.disconnect(cursor, db["conn"])
        return rows

    def disconnect(self, cursor, conn):
        """
        The function disconnects the cursor and connection objects.
        
        :param cursor: The cursor is an object that allows you to execute SQL queries and fetch results
        from the database
        :param conn: The `conn` parameter is a connection object that represents a connection to a
        database. It is used to establish a connection to the database and execute SQL queries
        """
        cursor.close()
        conn.close()
