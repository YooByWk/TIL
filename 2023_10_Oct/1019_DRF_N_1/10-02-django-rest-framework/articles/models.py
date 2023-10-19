from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 외래키는 N 이 가진다.
    # 하나의 게시글에 여러 글이 작성되는 구조기 때문
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 그 글이 사라지면 참조되던 댓글이 사라지는 옵션
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)