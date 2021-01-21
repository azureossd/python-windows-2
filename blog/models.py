from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=600, default='title')
    post_content = models.CharField(max_length=1024, default='content')
    tag = models.CharField(max_length=255,default='default')
    author = models.CharField(max_length=255,default='admin')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return super().__str__()

