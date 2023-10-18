from .models import Article
from .serializers import ArticleListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view # drf 규칙. 데코레이터를 달아라.

from .serializers import ArticleSerializer # 디테일 보는 serializers

from rest_framework import status #  상태코드

@api_view(['GET', 'POST']) # GET,POST 일때만 반응하는 함수라고 알림
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
    # 이제 파이썬만 다루는 것이 아닌, 유연한 데이터를 다룰 것. 
    # 따라서 serializer import 
    # many=True 해주셔야 해용
        return Response(serializer.data)
    # Response도 따로 임포트!
    # DRF view 함수에는 데코레이터가 필수적이다. 그렇지 않으면 작동하지 않음
    
    elif request.method == "POST": # ELSE 도 되지만 명시적으로 하기 위함: ELIF
        # form = ArticleForm(request.POST) 기존 방식
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사. 이름만 같은 뿐 (drf)
            serializer.save() # 이름만 같은것... 저장의 기능은 같다.
        return Response(serializer.data, status=status.HTTP_201_CREATED) # 상태코드 import
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 브라우저에서 뭔가 하긴 힘듬 -> 템플릿 음슴
    
    
    
@api_view(['GET', 'DELETE','PUT'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article) # 단일 이므로 Many X  // 기본이 many
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 삭제로 인해 content 가 없어요. 명확한 삭제 성공을 의미합니다.
    elif request.method=='PUT':
        # form = ArticleForm(request.POST, instance=article) # 기존
        serializer = ArticleSerializer(article, data=request.data)
        # form = ArticleForm(instance=article, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
    #실패했을 때
        return Response(status=status.HTTP_400_BAD_REQUEST)
    