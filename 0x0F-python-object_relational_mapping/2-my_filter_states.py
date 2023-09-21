#!/usr/bin/python3
"""Import modules"""
import MySQLdb
import sys

def list_states(username, password, db_name, state_name):
    """get all the states from the database"""
    name_searched = input()
    db = MySQLdb.connect(host="localhost", user=username, passwd=
                         password, db=db_name, port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC" .format(name_searched,))
    results = cur.fetchall()
    for res in results:
        print(res)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    list_states(username, password, db_name, state_name)
    sys.exit(0)
