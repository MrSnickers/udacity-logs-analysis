#!/usr/bin/env python3
#
# Prints reports

import psycopg2
import constants

def get_db(name):
    db = psycopg2.connect("dbname=%s" % name)
    return db

def get_results(db, query):
    try:
        cursor = db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        return results
    except Exception as exception:
        print (exception)

def print_results(title, query_results):
    print("========================= %s =========================" % title)
    for results in query_results:
        print ( "\t", results[0], "--", str(results[1]), "views")


if __name__ == '__main__':
    db = get_db("news")
    print_results(constants.ARTICLES_TITLE, get_results(db, constants.ARTICLES_QUERY))
    print("\n")
    print_results(constants.AUTHORS_TITLE, get_results(db, constants.AUTHORS_QUERY))
    db.close()