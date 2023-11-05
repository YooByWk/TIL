from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)



class CommentSerializer(serializers.ModelSerializer):
    # 여기서만 쓸꺼라서 ㅋㅋ.. 겹쳐도 됩니다.
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)

    # 오버라이드 할 것입니다.
    #################################################
    article = ArticleSerializer(read_only=True) # 아래의 코드는 문법적 오류가 발생
    #################################################
    # modelform과 비슷한것입니다.
    class Meta:
        model = Comment 
        fields = '__all__'
        # read_only_fields = ('article',) # 기본 필드에 대한 것


class ArticleSerializer(serializers.ModelSerializer):
    # 1 -> N 참조 중 // 댓글이 몇개건 다중 데이터가 나옴
    # 읽기 전용으로 변경할 것 / 이름 변경 불가능 / 역참조 매니저 이름 따라감
    comment_set = CommentSerializer(many=True, read_only=True)
    
    # 댓글 수 만큼 출력해주는 것
    # ArticleSerializer 는 article model에 기반해서 만들어집니다.
    # 이를 응용해서 아래에 넣어줍니다.
    # 얘도 read only
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        