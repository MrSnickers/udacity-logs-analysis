#!/usr/bin/env python3
#
# Prints reports

import psycopg2

def connect():
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        print ("connected!")
        db.close()
        print ("closed!")
    except:
        print ("Not connected")


if __name__ == '__main__':
    connect()