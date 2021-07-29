from django.contrib import admin
from blog.models import Post, BlogComments
# Register your models here.

admin.site.register((Post, BlogComments))
