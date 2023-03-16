#!/usr/bin/python3
"""
    Lis all cities from database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if len(sys.argv) < 4:
    print("Incorrect number of args passed.")
    print("USAGE: ./4-cities_by_state.py username password database")
    sys.exit(1)

usr, pswd, database = sys.argv[1], sys.argv[2], sys.argv[3]

with MySQLdb.connect("localhost", usr, pswd, database, 3306) as con:
    cur = con.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id
        ORDER BY cities.id""")
    res = cur.fetchall()
    for row in res:
        print(row)
