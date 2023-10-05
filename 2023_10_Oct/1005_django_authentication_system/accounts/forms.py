# articles forms 에서 import 돚거
# from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # 두개 임포트해서 커스텀 해줄겁니다.
# from .models import User # 이러지 마세요 . . . 동작은 하지만 좀 그래요.
from django.contrib.auth import get_user_model # 함수입니다.

class CustomUserCreationForm(UserCreationForm):
    # UserCreationForm을 상속받았어요!
    class Meta(UserCreationForm.Meta): # UserCreationForm의 meta만 덮어씁니다.
        model = get_user_model() # User Model을 get 한다! 아마? 
        # 장고에서 직접 참조보다, 간접적으로 하는 이유 :
        # get_user_model은 현재 프로젝트에서 활성화 된 사용자 모델(active user model)을 반환하는 함수
             

class CustomUserChangeForm(UserChangeForm):
    # UserCreationForm을 상속받았어요!
    class Meta(UserChangeForm.Meta): # UserCreationForm의 meta만 덮어씁니다.
        model = get_user_model()
        # 유저 대체가 진행되면, 어쩔 수 없이 진행되어야 한다.
        # N 번 유저를 찾을 필요가 없는 이유 : 그 사람은 이미 USER객체로 불러와져서
        # 이미 로그인 된 사람이 "스스로" 탈퇴하는거니까.
        fields = ('first_name', 'last_name', 'email') # 일반 사용자에게 이것만 하라고 제공해주는 field 임
        # 비밀번호는 여기 안됩니다. 아직은. 
        
        

