#!/usr/bin/python3
"""[summary]
    """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         charset="utf8")
    cur = db.cursor()
    # HERE I have to know SQL to grab all states in my database
    cur.execute(
        "SELECT name \
        FROM cities \
        WHERE state_id = \
            (SELECT id \
            FROM states \
            WHERE name = %s) \
            ORDER BY id ASC;", (sys.argv[4], ))
    query_rows = cur.fetchall()
    list1 = []
    for row in query_rows:
        list1.append(row[0])
    print(", ".join(list1))
    cur.close()
    db.close()
