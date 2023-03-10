from django.urls import path, include
from rest_framework import routers

from .views import UserArticleViewSet

router = routers.SimpleRouter()
router.register("article", UserArticleViewSet)


urlpatterns = [
    path('auth/', include('rest_auth.urls')),  # login/logout
] + router.urls
