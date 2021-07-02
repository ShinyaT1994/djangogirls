# DjangoのImport
from django.contrib import admin

# ModelのImport
from .models import Post

# Modelの登録
admin.site.register(Post)
