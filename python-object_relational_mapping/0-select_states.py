#!/usr/bin/python3
"""
    This module uses MySQLdb to access the database
    "database name"
"""
import MySQLdb
import sys

if len(sys.argv) < 4:
    print("Incorrect number of args passed.")
    print("USAGE: ./0-select_states.py username password database")
    sys.exit(1)

usr, pswd, database = sys.argv[1], sys.argv[2], sys.argv[3]

with MySQLdb.connect("localhost", usr, pswd, database, 3306) as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    res = cur.fetchall()
    for row in res:
        print(row)