from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list), # 이름은 템플릿에서 쓰던거라 지정 안했어요
    path('articles/<int:article_pk>/', views.article_detail),
]


