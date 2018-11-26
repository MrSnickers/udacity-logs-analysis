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
        return results
    except Exception as exception:
        print (exception)

def print_views(title, query_results):
    print("========================= %s =========================" % title)
    for result in query_results:
        name = result[0]
        number_of_views = str(result[1])
        print ( "\t %s  -- %s views" % (name, number_of_views))

def print_percentages(title, query_results):
    print("========================= %s =========================" % title)
    for result in query_results:
        date = result[0]
        number_of_errors = str(result[1])
        print ( "\t %s  -- %s %% errors" % (date, number_of_errors))


if __name__ == '__main__':
    db = get_db("news")
    print_views(constants.ARTICLES_TITLE, get_results(db, constants.ARTICLES_QUERY))
    print("\n")
    print_views(constants.AUTHORS_TITLE, get_results(db, constants.AUTHORS_QUERY))
    print("\n")
    print_percentages(constants.ERRORS_TITLE, get_results(db, constants.ERRORS_QUERY))
    db.close()