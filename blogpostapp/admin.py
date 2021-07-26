from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author','date_added')
    list_display_links = ('id', 'title')
    search_fields = ( 'title', 'slug', 'body', 'author','date_added')

class Contactadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Contact)