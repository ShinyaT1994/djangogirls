from django.conf import settings
from django.db import models
from django.utils import timezone

# 投稿モデル
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 著者
    title = models.CharField(max_length=200)    # タイトル
    text = models.TextField()   # 本文
    created_date = models.DateTimeField(default=timezone.now)   # 作成日
    published_date = models.DateTimeField(blank=True, null=True)    # 投稿日

    # ブログ公開メソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # タイトル呼び出しメソッド
    def __str__(self):
        return self.title
