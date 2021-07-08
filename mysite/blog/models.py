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

    # 承認されたコメントを取得
    def approved_comment(self):
        return self.comments.filter(approved_comment=True)

# コメントモデル
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    # コメントの承認
    def approve(self):
        self.approved_comment = True
        self.save()

    # コメント文呼び出し用
    def __str__(self):
        return self.text