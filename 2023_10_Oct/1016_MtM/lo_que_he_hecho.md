03-01-many-to-many

```py
# 한  일
# models.py

# Article 에
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL) # 추가
"""
ERRORS:
articles.Article.like_users: (fields.E304) Reverse accessor 'User.article_set' for 'articles.Article.like_users' clashes with reverse accessor for 'articles.Article.user'.
        HINT: Add or change a related_name argument to the definition for 'articles.Article.like_users' or 'articles.Article.user'.
articles.Article.user: (fields.E304) Reverse accessor 'User.article_set' for 'articles.Article.user' clashes with reverse accessor for 'articles.Article.like_users'.
        HINT: Add or change a related_name argument to the definition for 'articles.Article.user' or 'articles.Article.like_users'.
# 꾸엑

Article : User(N:1)
N:1 에서의 역참조
- user.article_set.all()

Article : User (N:M)
N:M 에서의 역참조
- user.article_set.all()
  
*이 두개 중복이니까 해결해줘*
"""
 like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like_articles")
 # N:M 참조의 이름을 바꿔서 해결했습니다.


# 좋아요 기능 구현
# url 작성
# articles.urls.py // 누가, 어디에 눌렀는가!
path('<int:article_pk>/likes/', views.likes, name='likes'),
# 좋아요 취소 \ etc를 위해 
# articles.views.py

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

# articles.templates index.html 
# 을 보려니 필요없는 like_users가 있으니 일단 제거를 위해 forms로 이동


# forms.py
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user', 'like_users',)

# index.html
<form action="{% url "articles:like" article.pk %}" method="POST">
  {% csrf_token %}
  {% comment %} 토글이 되야 함 {% endcomment %}
  {% if request.user in article.like_users.all %}
    <input type="submit" value='좋아요 취소'>
  {% else %}
    <input type="submit" value='좋아요'>
  {% endif %}
</form>
```