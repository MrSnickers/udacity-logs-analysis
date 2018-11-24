#!/usr/bin/env python3
#
# Prints reports

import psycopg2

def search():
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
        print ("connected!")
        cursor.execute("select articles.title, count(*) as views from articles inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by articles.title, log.path order by views desc limit 3")
        results = cursor.fetchall()
        db.close()
        print(results)
        return results
    except:
        print ("Not connected")


if __name__ == '__main__':
    search()