import datetime
from django.db import models

from  django.utils import timezone

class link(models.Model):
    link_name = models.CharField('name', max_length= 200)
    link_url = models.CharField('url', max_length= 200)
    link_views = models.IntegerField('views')
    def __str__(self):
        return self.link_url


class Article(models.Model):
    article_title = models.CharField('name', max_length=200)
    article_text = models.TextField('textpage')
    pub_date = models.DateTimeField('date')

    def __str__(self):
        return self.article_title
    def was_pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=10))

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE)
    author_name = models.CharField('authorname', max_length=50)
    comment_text = models.CharField('text', max_length=200)


class user_link(models.Model):
    link_author = models.CharField('authorname', max_length=150)
    link_name = models.CharField('name', max_length= 200)
    link_url = models.CharField('url', max_length= 200)
    link_views = models.IntegerField('views')
    def __str__(self):
        return self.link_url