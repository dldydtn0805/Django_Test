from django.urls import path
from . import views
# .을 안써도 작동하지만 장고에서는 명시적 상대경로로 . 을 작성하는 것을 선호한다

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('search/', views.search, name='search'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    # path('hello/<str:name>/',views.greeting),
    # str은 기본값이라 str 생략이 가능하다
    path('hello/<name>/',views.greeting),
    path('articles/<int:num>/', views.detail),
]
