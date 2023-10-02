from django.shortcuts import render, redirect
from .models import Article


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


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    article = Article(title=title, content=content)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)
    return redirect('articles:index')
    # return render(request, 'articles/create.html')
# render는 템플릿을 만들어서 보여주는 것.

def delete(request, pk ):
    # 몇 번 게시글을 삭제할 것인지 조회
    article = Article.objects.get(pk = pk)
    # 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = { 
            'article' : article
            }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 수정 게시글 조회 
    article = Article.objects.get(pk = pk)
    article.title = title
    article.content = content
    article.content = content
    article.save()
    
    return redirect('articles:detail', article.pk )