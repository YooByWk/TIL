from django.shortcuts import render, redirect

from django.views.decorators.http import require_http_methods # 3.,
from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm # 9.
# Create your views here.
from .forms import CustomUserCreationForm # 10


# import  로그인 로그아웃 
from django.contrib.auth import login  as auth_login
from django.contrib.auth import logout as auth_logout

# form : Auth form 로그인 용 form
from django.contrib.auth.forms import AuthenticationForm # 로그인 form

from django.contrib.auth.decorators import login_required

@require_http_methods(['GET','POST']) # 4.
def signup(request):
    # 1. 로그인한 사용자가 들어오면 
    # 2. 메인 화면으로 돌려보낸다
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    # 5. METHOD 가 GET 일 때와  POST 일 때
    
    # 6. POST : 회원가입을 진행시키는 "생성"입니다.
    
    # 8. 입력을 받고 싶다면 form , 하지만 이대로는 안된다. ! form 을 수정해주자
    if request.method == "POST": 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # 가입하면, 객체를 반환한다.
            auth_login(request, user)
            return redirect("boards:index")
        
    # 7. GET : 화면을 "보여"줍니다.
    else: 
        form  = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)
    # return render(request, 'accounts/signup.html', {'form':form}) 되긴 해요
    

@require_http_methods(['GET','POST'])
def login(request):
    # 로그인한 사용자가 온다면
    if request.user.is_authenticated:
        return redirect('boards:index')
    
    # 복붙했습니다.
    if request.method == "POST": 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
        
    else: 
        form  = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
    # return render(request, 'accounts/signup.html', {'form':form}) 되긴 해요    
    


# 세션 데이터를 지워야 함 == DB 를 건드린다 : POST
# @login_required
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("boards:index")