from django_filters import rest_framework as filters

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer
from .models import UserArticle
from .filters import ArticleFilter

# Create your views here.


class UserArticleViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer
    queryset = UserArticle.objects.all()[:10]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArticleFilter
