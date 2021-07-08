# DjangoのImport
from django.contrib import admin

# ModelのImport
from .models import Post, Comment

# Modelの登録
admin.site.register(Post)
admin.site.register(Comment)