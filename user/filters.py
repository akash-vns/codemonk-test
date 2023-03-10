from django_filters import rest_framework as filters
from .models import UserArticle


class ArticleFilter(filters.FilterSet):
    class Meta:
        model = UserArticle
        fields = {
            'content': ['icontains', ]
        }
