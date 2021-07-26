from django.db import models
from django.contrib.auth.models import  User
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title




class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    intro = models.TextField()
    body = models.TextField()   
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)


    def str(self):
        return self.title
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    messages = models.TextField()


    def __str__(self):
        return self.name
