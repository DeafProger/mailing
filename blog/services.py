from django.core.cache import cache
from blog.models import Blog

def get_blogs_from_cache():
    """
    Получение списка статей блога из кэша или БД.
    """
    key = 'categories_list'
    articles = cache.get(key)
    if articles is not None:
        return articles
    articles = Blog.objects.all()
    cache.set(key, articles)
    return articles
