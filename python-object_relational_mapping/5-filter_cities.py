#!/usr/bin/python3
"""
    List all cities from database hbtn_0e_4_usa from a given state
"""
import MySQLdb
import sys

if len(sys.argv) < 5:
    print("Incorrect number of args passed.")
    print("USAGE: ./5-filter_cities.py username password database name")
    sys.exit(1)

usr, pswd, database = sys.argv[1], sys.argv[2], sys.argv[3]
name = sys.argv[4]

with MySQLdb.connect("localhost", usr, pswd, database, 3306) as con:
    cur = con.cursor()
    cur.execute("""
        SELECT cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id AND
        BINARY states.name = %(name)s""", {"name": name})
    res = cur.fetchall()
    last_idx = len(res) - 1
    for idx, row in enumerate(res):
        if idx != last_idx:
            print(f"{row[0]}, ", end='')
        else:
            print(row[0])
