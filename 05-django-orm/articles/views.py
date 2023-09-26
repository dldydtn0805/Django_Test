from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    # 데이터베이스에서 전체 게시글을 조회
    articles = Article.objects.all()
    # 받은 전체 게시글 데이터를 변수에 담아 인덱스 템플릿에서 사용할 수 있도록 전달해야함
    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)