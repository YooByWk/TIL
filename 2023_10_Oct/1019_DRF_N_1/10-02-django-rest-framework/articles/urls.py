from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list), # 전체조회
    path('comments/<int:comment_pk>/', views.comment_detail),
    # path('articles/<int:article_pk>/comments/create', ) # URL에 행위에 대한 의미가 있는 것은 지양하자.
    path('articles/<int:article_pk>/comments/', views.comment_create ), # 행위는 POST 같은 method로 전송하자.

]
