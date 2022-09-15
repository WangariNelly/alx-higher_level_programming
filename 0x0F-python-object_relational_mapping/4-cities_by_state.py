#!/usr/bin/python3
"""
Script that lists all the cities from database
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    sql = (
        "SELECT c.id, c.name, s.name FROM \
        cities as c INNER JOIN \
        states as s ON \
        c.state_id = s.id \
        ORDER BY c.id"
    )
    cur = conn.cursor()
    cur.execute(sql)
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
