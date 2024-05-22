from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"
        db_table = 'categories'


class News(models.Model):
    news_title = models.CharField(max_length=255, unique=True)
    news_description = models.CharField(max_length=255)
    news_image = models.ImageField(upload_to='news/')
    news_content = models.TextField()
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    news_pub_date = models.DateTimeField(auto_now_add=True)
    news_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name_plural = "News"
        db_table = 'news'
