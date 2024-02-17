#!/usr/bin/python3

import MySQLdb
import sys


def list_states(mysql_username, mysql_password, database_name):

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
       print(row)

    db.close()
