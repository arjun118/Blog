# from turtle import title
from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title= models.CharField(max_length=255)
    body= models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
    
    def get_absoulute_url(self):
        return reverse("article_detail",kwargs={"pk":self.pk})


# Note that there are two main ways to refer to a custom user model: AUTH_USER_MODEL and get_-
#  As general advice:
# • AUTH_USER_MODEL makes sense for references within a models.py file
# • get_user_model() is recommended everywhere else such as views, tests, etc.

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse("article_list")
