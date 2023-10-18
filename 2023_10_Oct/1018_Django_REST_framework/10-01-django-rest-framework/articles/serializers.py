from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 해당 모델
        fields = ('id', 'title', 'content',) 
        # 어떤 필드를 보여줄것인가.
        # 이름이 꼭 이것도 아니고, 꼭 여기에 없어도 됨. 그냥 여기에 두고 편하게 관리하자는 의미
      
      
# 전체 필드 출력용  
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'