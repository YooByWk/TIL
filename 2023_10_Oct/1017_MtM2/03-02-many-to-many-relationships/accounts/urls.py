from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('<username>/', views.profile, name='profile')
    # 이러면 어떤 str이건간에 username으로 받아 버리기 때문에 아래의 url을 사용하지 못할수도 있음
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
