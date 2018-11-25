ARTICLES_QUERY = "select articles.title, count(*) as views from articles inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by articles.title, log.path order by views desc limit 3"
ARTICLES_TITLE = "Most Popular Articles"
AUTHORS_QUERY = "select authors.name, count(*) as views from articles inner join authors on articles.author = authors.id inner join log on log.path like concat('%', articles.slug, '%') where log.status like '%200%' group by authors.name, log.path order by views desc limit 3"
AUTHORS_TITLE = "Most Popular Authors"