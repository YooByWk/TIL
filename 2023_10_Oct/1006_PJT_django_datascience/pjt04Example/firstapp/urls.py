from django.urls import path

from . import views

# 다른앱의 뷰를 가져와도 무관.

# app_name = 
urlpatterns = [
    # how to connect each files.
    # view -> DB (Models)
    # view -> input -> Form
    # view -> print smth == templates
    # path=('',views.index, name='index'),
    path('',views.index), # 앱이 하나라 구분 필 없을듯
    path('example/', views.example),
]
