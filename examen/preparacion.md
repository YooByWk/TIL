# 2023_10_02
## 시험준비 & Django ORM & etc.


## django ORM

### QuerySet API
#### orm에서 데이터를 검색 필터링 정렬 및 그룹화 하는데 사용하는 도구
- api 사용, sql이 아닌 python 코드로 데이터 처리
- api 인 이유 : 장고 - DB의 소통이기 때문!

#### QuerySet API
python의 set은 아님.

#### queryset api 구문
Article.objects.all()
- 순서대로
  - Model class
  - Manager (아래의 메서드를 사용하기 위한 매니저, 여기가 method 를 가지고 있다.)
  - 이상까지는 주로 예외 없이 (Model명(*class 명*).objects.) 까지는 동일하다.
  - Queryset API (메서드)

#### Query
- DB에 특정한 데이터를 보여달라는 요청
- "쿼리문 작성" == 원하는 데이터를 얻기 위해 데이터 베이스에 요청을 보낼 코드를 작성한다.
- 파이썬을 ㅗ작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터 베이스의 응답 데이터를 ORM이 queryset이라는 자료 형태로 변환하여 우리에게 전달한다.

#### QuerySet
- DB에게서 전달받은 객체 목록(데이터 목록)
  - 순회가 가능한 데이터로, 1개 이상의 데이터를 불러와 사용할 수 있다.
  - == for 사용 가능!!
- Django ORM을 통해 만들어진 자료형
- 단 DB가 단일 객체를 반환한다면 QuerySet이 아닌 Model(class)인스턴스로 반환. 

목표 : Python의 Model class와 instance를 활용해,CRUD to DB

<hr>
'django_extensions' - 서드파티라서 settings.py 에 등록해야해요.
깔고나서 requirements.txt 업데이트 까먹지마세요

```bash
pip freeze > requirements.txt
```
 #### app 등록 "권장" 순서
  1. normal app
  'articles',
  2. third party app
  'django_extensions',
  3. django app
뒤쥭박쥭 해도 큰 일 없지만, 나중에는 몰?루

#### Django shell
Django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미친다.
- extensions에 shell-plus를 쓸 것임!

**python manage.py shell_plus**/ Django shell 실행/  shell 이랑 다르게, 이것저것 바로 싹다 Import하고 시작합니다. 자동완성에도 차이가 있다.
- 뭔가 엄청 나옵니다. (django extensions)
- 엄청나게 import 하고 있습니다.
- 나가는 법 exit 입력
- 터미널 정리 ctrl + L

데이터 객체를 만드는 방법 :
- view 함수에서 할 것입니다.
- 클래스 연습 >  shell 에서 연습 > 그다음 view 

## 데이터 생성 Create
### 1번째 방법
shell 입력창입니다.
```python 
In [1]: article = Article()

In [2]: article
Out[2]: <Article: Article object (None)>

In [3]: article.title ='first'

In [4]: article.title
Out[4]: 'first'

In [5]: article.content = 'django!'

In [6]: article.content
Out[6]: 'django!'

In [6]: article.save()

In [9]: Article.objects.all()
Out[9]: <QuerySet [<Article: Article object (1)>]>

In [10]: articles = Article.objects.all()

In [11]: articles
Out[11]: <QuerySet [<Article: Article object (1)>]>

In [12]: articles[0]
Out[12]: <Article: Article object (1)>

In [13]: article.id
Out[13]: 1
# pk 참고
In [14]: article.title
Out[14]: 'first'

In [15]: article.content
Out[15]: 'django!'

In [16]: article.created_at
Out[16]: datetime.datetime(2023, 10, 2, 11, 14, 44, 642944, tzinfo=datetime.timezone.utc)  

In [18]: article.pk
Out[18]: 1
# 장고는 id보다 pk를 주로 사용합니다. primary key
```
article.all()  = 전체 조회 - 쿼리셋만 받음 
- 단일 데이터라고 생각하면 index error 다분 // 데이터가 하나라도! 하나라고 생각하지 마쇼!

### 두번쨰 방법

```python
In [21]: article.title
Out[21]: 'second'

In [22]: article.pk

# 저장을 안해서 pk값이 없다.  

# 아래는 저장

In [23]: article.save()

In [24]: article.pk

Out[24]: 2

```

### 세번째 방법
``` python
In [26]: Article.objects.create(title='third', content='django')
Out[26]: <Article: Article object (3)>


```
save() - 객체를 저장하는 메서드

## 데이터 조회 Read
all()
- 전체 데이터 조회f
```python 
In [35]: Article.objects.all()
Out[35]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

In [36]: for article in articles:
    ...:     print(article.title)
    ...:
# [out]
first
second
third
```

get() - 단일 데이터 조회
- 하나 이상의 조건 만족 == get() returned more than on Article 이렇게 장고가 극대노합니다.
- pk에 상당히 적합한 method

- 객체를 찾을 수 없으면 DoesNotExist 예외
- 둘 이상의 객체를 찾는다면,  MultipleObjectsReturned 예외
- 위와 같은 특징으로 인해 primary key 같이 고유성을 보장하는 것에 사용

```python
In [37]: Article.objects.get(pk=1)
Out[37]: <Article: Article object (1)>

In [38]: Article.objects.get(pk=15464)
# DoesNotExist: Article matching query does not exist.

################
```

filter() - 특정조건 데이터 조회
- 
```python

In [40]: Article.objects.filter(content='django')
Out[40]: <QuerySet [<Article: Article object (3)>]>

In [41]: Article.objects.filter(content='ssafy')
Out[41]: <QuerySet []>

In [42]: # 조건을 만족하지 않는다면, 빈 QuerySet을 반환한다. 

In [43]: Article.objects.filter(title='first')
Out[43]: <QuerySet [<Article: Article object (1)>]>

# 한 개만 포함한다고 해도, 쿼리셋으로 반환.
```

## UPDATE  수정.
- 수정을 위해서는 조회를 해야한다. get()
```python

In [44]: article = Article.objects.get(pk=1)

In [45]: article.title = 'byebye'

In [46]: article.title
Out[46]: 'byebye'

In [47]: # 아직 db에는 저장 안됨 !

In [48]: # instance에서 노는중

In [49]: article.save() # 수정 완료

# delete 
# 엥 바로되네
In [50]: article.delete()
Out[50]: (1, {'articles.Article': 1})


#  
In [51]: articles.delete() # 싹 다 지워지네요? 
Out[51]: (2, {'articles.Article': 2})

```
# 흑흑 공식문서를 봐 주세요
# 쪠빨


### Field lookups
- 특정 레코드에 대한 조건을 설정하는 방법
- queryset 메서드 filter(), exclude(), get() 에 대한 키워드 인자로 지정된다.
<p>
</p>

ex
```shell
Article.objects.fliter(content__contians='dja')

# 조건을 만족하는 것을 다 보여주는 듯
In [52]: Article.objects.filter(pk__gt=4)
Out[52]: <QuerySet []>
# gt : greater than
```
### ORM, QuerySet API 사용 이유
- 데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용 하지 않아도 되도록
- 데이터 베이스와의 결합도를 낮추고 개발자가 더욱 *직관적이고 생산적*으로 개발할 수 있도록 도움
- 프레임워크를 쓰는 이유니까요?
- 우리는 *python을* 쓰고 있다는 사실을 잊으면 안돼요.
- 파이썬에 장고의 규칙만 조금 더한 것일 뿐


### 제약조건은 어... 알아서 지 혼자 shell 에서 통과할수도 있음
- "유효성 검사"

### 실제 활용
- 메인 페이지 전체 게시글 출력 all() 

url - views - html 순의 흐름 작성.

view 에서 db 조회
> 변수에 담아서 템플릿에서 사용할 수 있게 만들어주기.
```python 
# models.py에서 불러오기
from .models import Article

def index(request):
  articles = Article.objects.all()

  # 템플릿에서 사용가능하게 전달
  context ={
    'articles : articles,
  }
  return render(request, 'index.html', context)


# index.html
# QuerySet은 반복(for) 가능!!
{% for article in articels %}
  {{ article.title }}
  {{ article.content }}
{% endfor %}

```
CRUD 의 본격적 시작!! 20230915
