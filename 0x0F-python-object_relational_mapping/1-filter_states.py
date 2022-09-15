#!/usr/bin/python3
"""
This scripts prints all states with a name starting with N
(upper N) from database hbtn_0e_0_usa.
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    sql = ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    cur = conn.cursor()
    cur.execute(sql)
    states = cur.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    cur.close()
    conn.close()
