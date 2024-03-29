#!/usr/bin/python3
"""Import modules"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """get all the states from the database"""
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    list_states(username, password, db_name)
    sys.exit(0)
