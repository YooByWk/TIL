from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid:
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@login_required
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


def likes(request, article_pk):
    # 별도의 페이지는 필요 없을 듯 - 게시글 출력 페이지에 좋아요 버튼이 같이 출력됨
    # if request.method == 'POST': # 필요 없다
    # 어떤 게시글에 좋아요를 누른건지
    article = Article.objects.get(pk=article_pk) # 게시글을 가져왔어요
    
    # 좋아요 or 취소 판단
    # 현재 좋아요 버튼을 누른 유저가 어디(현재 게시글의 좋아요를 누른 유저 목록 전체)에 있는지 없는지를 확인.
    # 이미 누른 사람들을 찾아보자.
    if request.user in article.like_users.all():  # like_user은 아까 model에서 바꾼 역참조 manager 이름
        # 취소 1 # 사람의 좋아요 게시글 중 에서 삭제 ?
        # request.user.like_articles.remove(article) 
        # 취소 2 # 다대다 관계라서 문제가 없다.  # 게시글의 사람 목록 중 삭제 ? 어차피 위아래 같은걸
        article.like_users.remove(request.user)
    else: 
        # 반대
        article.like_users.add(request.user)
        # request.user.like_articles.add(article)
    return redirect('articles:index')