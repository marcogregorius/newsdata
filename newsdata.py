#!/usr/bin/python3

import psycopg2
import datetime


def mostPopularArticles():
    '''
    Query to return the most popular three articles of all time
    '''
    pg = psycopg2.connect(dbname="news")
    c = pg.cursor()
    c.execute("""SELECT
              articles.title,
              count(log.id) as num
              FROM articles, log
              WHERE articles.slug = substring(log.path, 10)
              GROUP BY articles.title
              ORDER BY num DESC
              """)
    results = c.fetchall()
    print("Most popular three articles of all time:")
    for article in results:
        print(article[0] + " - " + str(article[1]) + " views")
    c.close()


def mostPopularAuthors():
    '''
    Query to return the most popular authors of all time
    '''
    pg = psycopg2.connect(dbname="news")
    c = pg.cursor()
    c.execute("""SELECT
                 authors.name,
                 count(log.id) as num
                 FROM authors, log, articles
                 WHERE articles.slug = substring(log.path, 10)
                 AND articles.author = authors.id
                 GROUP BY authors.name
                 ORDER BY num DESC
                 """)
    results = c.fetchall()
    print("\nMost popular authors of all time:")
    for author in results:
        print(author[0] + " - " + str(author[1]) + " views")
    c.close()


def daysWithHighErrors():
    pg = psycopg2.connect(dbname="news")
    c = pg.cursor()
    c.execute("""SELECT
                AggregateOK.date,
                CAST(AggregateError.numerror AS float)/AggregateOK.num
                AS ErrorRate
                FROM
                (
                SELECT
                time::date as date,
                count(id) as num
                FROM log
                GROUP BY date
                ) AS AggregateOK,
                (
                SELECT
                time::date as date,
                count(id) as numerror
                FROM log
                WHERE left(status, 1) = '4' OR left(status, 1) = '5'
                GROUP BY date
                ) AS AggregateError
                WHERE AggregateOK.date = AggregateError.date
                AND
                CAST(AggregateError.numerror AS float)/AggregateOK.num > 0.01
                ORDER BY AggregateError.numerror DESC
                """)

    results = c.fetchall()
    print("\nDays that more than 1% of requests led to errors:")
    for data in results:
        date_long = datetime.datetime.strptime(str(data[0]), '%Y-%m-%d')
        print(date_long.strftime('%B %d, %Y') +
              " - " +
              "{:.1%}".format(data[1]) + " errors")
    c.close()


mostPopularArticles()
mostPopularAuthors()
daysWithHighErrors()
