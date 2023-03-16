#!/usr/bin/python3
"""
    This module uses MySQLdb to access a database
    and returns all elements in the states table that start
    with "N"
"""
import MySQLdb
import sys

if len(sys.argv) < 4:
    print("Incorrect number of args passed.")
    print("USAGE: ./1-filter_states.py username password database")
    sys.exit(1)

usr, pswd, database = sys.argv[1], sys.argv[2], sys.argv[3]

with MySQLdb.connect("localhost", usr, pswd, database, 3306) as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    res = cur.fetchall()
    for row in res:
        print(row)