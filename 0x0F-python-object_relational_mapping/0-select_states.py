#!/usr/bin/python3

"""This script prints all the states in hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == '__main__':
    connection = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306
        )
    cur = connection.cursor()
    sql = ("SELECT * FROM states ORDER BY id ASC")
    cur.execute(sql)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    connection.close()
