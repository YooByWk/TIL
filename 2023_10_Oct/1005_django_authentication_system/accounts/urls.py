from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name="delete"),
    path('update/', views.update, name="update"),
    # path('<int:user_pk>/password/', views.password, ) 여기서 하면 안됨 PJT url로 가시오.
]
