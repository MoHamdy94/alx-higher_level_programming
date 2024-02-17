#!/usr/bin/python3

import MySQLdb
import sys


def list_states_starting_with_n(mysql_username, mysql_password, database_name):
    """Connects to the MySQL database,
    lists states with names starting with 'N'
    in ascending order of ID, and closes the connection.
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
