#!/usr/bin/python3
"""Import modules"""
import MySQLdb
import sys

def list_states(username, password, db_name, state_name):
    """get all the states from the database"""
    db = MySQLdb.connect(host="localhost", user=username, passwd=
                         password, db=db_name, port=3306)

    cur = db.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name, ))
    results = cur.fetchall()
    for res in results:
        print(res[0])
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    list_states(username, password, db_name, state_name)
    sys.exit(0)
