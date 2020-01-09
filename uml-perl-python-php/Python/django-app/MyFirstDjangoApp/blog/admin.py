from django.contrib import admin

# Register your models here.
from MyFirstDjangoApp.blog.models import posts

admin.site.register(posts)