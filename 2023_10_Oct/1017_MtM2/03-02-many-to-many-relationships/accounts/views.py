from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth import get_user_model
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


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username): # 라우팅으로 url에서 들어오는중 
    # 유저의 디테일 페이지 
    # request.user 안하는 이유 : 로그인 한 유저만 볼 수 있음
    # user 조회 : getusermodel
    User = get_user_model()
    person = User.objects.get(username=username) #네놈의 페이지구나! 
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


def follow(request, user_pk):
    # follow를 하는 대상을 조회한다.
    User = get_user_model() # 당할 사람 가져오는 방법
    you = User.objects.get(pk=user_pk) # 당할사람 ; ; ; # url 상 아마도 피해자가 될 유저의 정보인듯
    me = request.user # 나 ; ; ; # 요청을 누를 사람
    
    # 자기 자신 팔로우 하면 안되니까
    if me != you:
            
        # 팔로우 취소 / 진행에 대한 기준
        # 구현이 힘들면 articles 의 좋아요 구경해보기
        if me in you.followers.all():
            # 내가 상대방의 팔로워 목록에 있다면,  팔로우 취소
            you.followers.remove(me)
            # == me.followings.remove(you)
        else:
            you.followers.add(me)
            # me.folliwngs.add(you)
    return redirect('accounts:profile', you.username)
    
