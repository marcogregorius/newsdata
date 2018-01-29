# README
## Introduction
The database in this project consists of 3 tables, a list of articles with number of views, authors of the articles and request status codes of the website.

This code is designed to query with regards to three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Usage
1. Download the [dataset](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file and put it in the same folder as newsdata.py
2. Generate the data into your local database using command `psql -d news -f newsdata.sql`.
3. Run newsdata.py to call the function `mostPopularArticles()`, `mostPopularAuthors()`, `daysWithHighErrors()` in *newsdata.py* to answer above questions respectively.

## Result
Output of above queries can be found in `output.txt`


