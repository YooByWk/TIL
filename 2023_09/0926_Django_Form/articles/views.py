from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request): # new 가 아래로 병합될 예정입니다.
#     form = ArticleForm() # 인스턴스
#     context = {
#         'form': form, 
#     }
#     return render(request, 'articles/new.html', context)

# CRUD 의 C 의 최종 진화
def create(request):
    # 요청의 메서드가 POST라면 (create)
    # articleform을 통해서 데이터가 들어오고 있다.
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 한번에 싹 다 받아요.
        # 유효성 검사 진행
        if form.is_valid(): # 유효하다면? T / F 
        # 유효성 검사가 통과된 경우
            article = form.save() # 저장합니다.
            # 저장이 올바르게 됐다면!!!
            return redirect('articles:detail', article.pk)
            # article은 지금 막 생성된 친구임.
            # save또한 return이 있기 때문에 article 객체로.
            
            
    # 요청의 메서드가 POST가 아니라면 (new)
    # post, get 말고도 다른게 있으니까, method 가 2개가 더있어요
    # get = R , post = CUD ( U, D 는 다른 method 가 있음. )
    # ! 반 ! 드 ! 시 ! POST 일때만 하세요 !!!!!!!
    else: # 헉 
        form = ArticleForm()
        
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
    # redirect 하면 안됨, 그 페이지로 돌아가는 것이 아니라, 해당 에러가 담긴
    # 페이지를 새로 만듭니다.
    
    
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')
#기존 코드입니다.
##################################################
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

##################################################
# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

# edit 과 update 도 합쳐집니다. 우와 
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청의 메서드가 POST라면 (update)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        # data가 첫번째 인자라서 data라고 안써서 생략헀던거임 
        # instance의 경우 꽤나 뒤에있어서 이상하게 들어감 
        # instance대신 files=article이 될지도 모른다. 
        # 기존의 값을 instance로 넣음.
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    # 요청의 메서드가 POST가 아니라면 (edit) CRUD 中   R
    else: # edit # 순서에 신경써보자. 
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
