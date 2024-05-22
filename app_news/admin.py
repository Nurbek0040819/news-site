from django.contrib import admin

from app_news.models import News, Category

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
