from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_photo')
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    article = models.ForeignKey(Article, related_name='article_category', on_delete=models.CASCADE)
    cat = models.CharField(max_length=100) 

    