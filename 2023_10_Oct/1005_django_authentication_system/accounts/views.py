from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# 데코레이터가 미리 한번 작동 전에 일합니다.
# @login_required 로그인 여부  articles views로 

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def signup(request):
    # req method 에 따라서 역할이 두 개
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) # 모델폼이라서 첫 위치가 데이터임.
        # form = UserCreationForm(data = request.POST) # 모델폼이라서 첫 위치가 데이터임. 얘는 Model Form
        # form = AuthenticationForm(request, request.POST) # 인자 순서 비교를 위함, 얘는 Form
        
        # 유효성 검사
        if form.is_valid():
            form.save() # DB 저장. Shell 생각해보기!
            return redirect('articles:index')
        
    else:
        form = CustomUserCreationForm()
    context={
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    # 로그아웃과 유사함 - 
    # 유저 객체의 method 中 delete, 근데 user 객체는 어디에 ? ? ? ?
    request.user.delete()
    # request 안에 user가 있고, delete method를 가져요.
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance = request.user ) # 인스턴스는 현재 유저 정보입니다.
        # 수정 로직에는 하나 더 들어갑니다. 기존 객체가 필요하거든요.
        # 저장의 갱신인지, 새로 저장인지를 알기 위함
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance = request.user) # instance가 들어있어서 기존 정보가 나온다. 
    context={
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk): # 라우팅으로 정보도 받아와요
    # change_password 한 이유는 혹시 모를 이름 중복 방지
    # 
    if request.method == "POST": 
        form = PasswordChangeForm(request.user, request.POST) # 이것 자체가 수정되는 . . . So just take POST from user
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user )
            return redirect('articles:index')
    else: 
        # SetPasswordForm 이라는 부모가 있어요 but  첫 인자로 user object를 받아야 한다. 
        form = PasswordChangeForm(request.user) #  필수 위치인자 : 유저 객체 必
    
    context={
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
