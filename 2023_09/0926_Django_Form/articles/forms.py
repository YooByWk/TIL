from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # model을 등록만 하면 됩니다.
    class Meta: # 내부 클래스임. 장고의 문법이라고 보면 될듯
        model = Article # 필 수, model의 article 클래스를 가져온 것
        fields = '__all__' # 필 수  # 그 중 어떤것을 사용할 것인가.
        # fields = ('tltle',) # 이 놈만
        # exclude = ('title',) # 이 놈 빼고 

        # 언더바 언더바 all 언더바 언더바
        # or 쓰고싶은 필드
        # 표기상의 문법임. 깊게 들어갈 필요 없습니다.
    # meta는 메타데이터라고 함. 어떠한 데이터에 대한 데이터.
    # 아티클(앱) 폼에 대한 데이터. // 정보에 대한 정보

# formfield 및 widget 활용
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/
# https://docs.djangoproject.com/en/4.2/topics/forms/
# https://docs.djangoproject.com/en/4.2/ref/forms/widgets/

# 구성이 마음에 안든다면?
# 별도의 위젯이 필요합니다!


# 위젯 등록하려고 . . .
class ArticleForm(forms.ModelForm):
    title = forms.CharField( # django formfield입니다.
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', # 클래스 지정. 부트스트랩 가능할듯
                'placeholder': 'Enter the title', # 
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력해주세요.'
        }
    )

    # model 등록
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)
