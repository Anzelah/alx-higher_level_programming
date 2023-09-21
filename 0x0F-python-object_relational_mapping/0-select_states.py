#!/usr/bin/python3
"""Import modules to use"""
import MySQLdb
import sys
"""Imported modules to use"""


def list_states(username, password, db_name):
    """get all the states from the database"""
    db = MySQLdb.connect(host="localhost", user=username, passwd=p
                         assword, db="hbtn_0e_0_usa", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()
    for res in results:
        print(res)

    cur.close()
    db.close()


if __name__ == "__main__":
    """Prevent exprtation."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
    sys.exit(0)
