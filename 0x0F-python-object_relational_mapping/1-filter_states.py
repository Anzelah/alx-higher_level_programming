#!/usr/bin/python3
"""Import modules"""
import MySQLdb
import sys

def filter_states(username, password, db_name):
    """get all the states from the database"""
    db = MySQLdb.connect(host="localhost", user=username, passwd=
                         password, db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT * FROM states WHERE NAME LIKE 'N%' ORDER BY states.id ASC")
    results = cur.fetchall()
    for res in results:
        if ("N" in res):
            print(res)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    filter_states(username, password, db_name)
    sys.exit(0)
