#!/usr/bin/python3
import MySQLdb
import sys


def connect_database_5(usr, paswd, dt_name, st_name):
    """ connects with
    database to
    gather information"""
    times = 1
    db = MySQLdb.connect(host='localhost', user=usr, passwd=paswd,
                         db=dt_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c\
    JOIN states s ON s.id = c.state_id WHERE s.name = '{}'\
    ORDER BY c.id ASC".format(st_name))
    res = cur.fetchall()
    for state in res:
        if times < len(res):
            print("{}, ".format(state[0]), end="")
        else:
            print("{}".format(state[0]))
        times += 1
    cur.close()
    db.close()


if __name__ == "__main__":
    """ Exectues if
    main is calling it"""
    try:
        if sys.argv[4]:
            connect_database_5(sys.argv[1], sys.argv[2], sys.argv[3],
                               sys.argv[4])
    except:
        pass
