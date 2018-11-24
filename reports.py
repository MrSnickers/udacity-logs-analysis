#!/usr/bin/env python3
#
# Prints reports

import psycopg2
import queries

def get_db(name):
    db = psycopg2.connect("dbname=%s" % name)
    return db

def get_results(db):
    try:
        cursor = db.cursor()
        cursor.execute(queries.ARTICLES)
        results = cursor.fetchall()
        print(results)
        return results
    except:
        print ("Not connected")

if __name__ == '__main__':
    db = get_db("news")
    get_results(db)
    db.close()