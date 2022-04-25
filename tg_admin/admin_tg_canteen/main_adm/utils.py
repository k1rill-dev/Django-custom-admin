from django.core.cache import cache
from django.db.models import Count

from .models import *

class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        # categories = cache.get('categories')
        if not categories:
            categories = User.objects.annotate(Count('blog'))
            # cache.set('categories', categories)

        # categories = Category.objects.annotate(Count('blog'))
        # context['menu'] = menu
        context['users'] = users
        return context