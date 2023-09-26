from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인페이지를 응답
    return render(request, 'articles/index.html')
# request는 필수적으로 들어가는 약속된 인자이다
# 뒤에 index.html은 템플렛의 경로이다