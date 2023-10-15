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
    article = Article.objects.get(pk=pk) # 외래 키 데이터 # 디테일마다 다른 것
    comment_form = CommentForm()
    # 특정 게시글의 모든 댓글을 조회(역참조)
    comments = article.comment_set.all() # 해당 article 인스턴스의 댓글만 조회할 것임
    # comments = Comment.objects.all() # 이러지 마세요. '모든' 댓글임
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
            article = form.save()
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
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# def comments_create(request, pk):
#     # 게시글 조회
#     article = Article.objects.get(pk=pk)
#     # CommentForm으로 사용자로 부터 데이터를 입력 받음
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.article = article
#         comment_form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article': article,
#         'comment_form': comment_form,
#     }
#     return render(request, 'articles/detail.html', context)


# def comments_delete(request, article_pk, comment_pk):
#     # 댓글 조회
#     comment = Comment.objects.get(pk=comment_pk)
#     comment.delete()
#     return redirect('articles:detail', article_pk)

def comments_create(request, pk): # 이곳에는 항상 POST 요청만 들어온다. get post 나눌 이유 없음.
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # CommentForm으로 사용자로 부터 데이터를 입력받음
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 저장은 아직 하지 않으나, 인스턴스는 제공해줌!
        comment.article = article # 해당 게시글에 묶어준 것 같아요
        comment_form.save() # 진짜 저장
        return redirect('articles:detail', article.pk)

    context= {
        'article' : article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

# @login_required
# def comments_delete(request, comment_pk):
#     comment = Comment.objects.get(pk=comment_pk)
#     article_pk = comment.article.pk # comment를 이용하여 article의 pk를 알아내자
#     comment.delete()
#     return redirect('articles:detail', )
#     # articles 에 redirect 하기 위해서는 필요하다 article의 pk 
#     # 교재랑 다르긴 하지만 되는구나!
#     # url에서 pk를 가져올 수 있다면 설계 측면에서 권장된다.
#     # 통일성이 조금 떨어질 뿐 다시 갑니닷.
#     # url 수정하고 오겠습니다.

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk # comment를 이용하여 article의 pk를 알아내자
    # url 변경되어 필요 없다.
    comment.delete()
    return redirect('articles:detail', )
    # articles 에 redirect 하기 위해서는 필요하다 article의 pk 
    # 교재랑 다르긴 하지만 되는구나!
    # url에서 pk를 가져올 수 있다면 설계 측면에서 권장된다.
    # 통일성이 조금 떨어질 뿐 다시 갑니닷.
    # url 수정하고 오겠습니다.