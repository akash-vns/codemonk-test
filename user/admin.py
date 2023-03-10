from django.contrib import admin
from .models import User, UserArticle
# Register your models here.

admin.site.register([User, UserArticle])
