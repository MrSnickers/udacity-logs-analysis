ARTICLES_QUERY = "select articles.title, count(*) as views from articles inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by articles.title, log.path order by views desc limit 3"
ARTICLES_TITLE = "Most Popular Articles"
AUTHORS_QUERY = "select authors.name, count(*) as views from articles inner join authors on articles.author = authors.id inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by authors.name, log.path order by views desc limit 3"
AUTHORS_TITLE = "Most Popular Authors"
ERRORS_QUERY = "select day, perc from (select day, round((sum(requests)/(select count(*) from log where substring(cast(log.time as text), 0, 11) = day) * 100), 2) as perc from (select substring(cast(log.time as text), 0, 11) as day, count(*) as requests from log where status like '%404%' group by day)as log_percentage group by day order by perc desc) as final_query where perc >= 1"
ERRORS_TITLE = "Days with more than 1% errors"

