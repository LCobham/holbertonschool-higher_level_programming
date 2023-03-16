#!/usr/bin/python3
"""
    This module uses MySQLdb to access a database
    and returns all elements in the states table that
    match a name passed as a command line arg. Safe from
    SQL injections.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Incorrect number of args passed.")
        print("USAGE:" +
              "./3-my_safe_filter_states.py username password database name")
        sys.exit(1)

    usr, pswd, database = sys.argv[1], sys.argv[2], sys.argv[3]
    name = sys.argv[4]

    with MySQLdb.connect("localhost", usr, pswd, database, 3306) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM states WHERE BINARY name = %(name)s",
                    {"name": name})
        res = cur.fetchall()
        for row in res:
            print(row)
