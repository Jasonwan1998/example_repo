select owner.owner_id, owner.owner_name, count(category_article_mapping.category_id)
from owner, article, category_article_mapping
where owner.owner_id = article.owner_id and article.article_id = category_article_mapping.article_id;