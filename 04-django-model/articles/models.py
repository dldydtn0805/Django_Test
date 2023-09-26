from django.db import models

# Create your models here.

class Article(models.Model):
# Model의 모든 속성을 Article에 상속받는다.
    title = models.CharField(max_length=10)
    #최대 길이가 10
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 위 둘의 키워드 인자의 기본값은 False임을 추측 가능