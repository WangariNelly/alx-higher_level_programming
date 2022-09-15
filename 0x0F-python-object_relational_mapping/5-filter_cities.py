#!/usr/bin/python3
"""
This script lists all cities in a state. The state
is passed as an argument
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
    city_arg = argv[4]
    sql = (
        "SELECT cities.name FROM cities JOIN \
        states ON cities.state_id = states.id \
        WHERE states.name LIKE %s ORDER BY cities.id \
        ".format(city_arg)
    )
    cur = conn.cursor()
    cur.execute(sql, (city_arg,))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    conn.close()
