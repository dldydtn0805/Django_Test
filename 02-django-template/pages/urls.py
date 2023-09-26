from django.urls import path
from . import views
# .을 안써도 작동하지만 장고에서는 명시적 상대경로로 . 을 작성하는 것을 선호한다

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
]
