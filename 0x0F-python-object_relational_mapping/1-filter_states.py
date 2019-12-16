#!/usr/bin/python3
import MySQLdb
import sys


def connect_database_1(usr, paswd, dt_name):
    """ connects with
    database to
    gather information"""
    db = MySQLdb.connect(host='localhost', user=usr, passwd=paswd,
                         db=dt_name, port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    res = cur.fetchall()
    for state in res:
        if state[1][0] == 'N':
            print(state)
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Exectues if
    main is calling it"""
    try:
        if sys.argv[3]:
            connect_database_1(sys.argv[1], sys.argv[2], sys.argv[3])
    except:
        pass
