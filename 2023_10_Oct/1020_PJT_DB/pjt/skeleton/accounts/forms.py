from django.contrib.auth.forms import UserCreationForm
# 방법 1. 
from .models import User # 권장하지 않고, 버그도 잦음
# 방법 2. settings 의 AUTH_USER 가져오는 것
from django.conf import settings # settings.AUTH_USER_MODEL 
# -> 문자열 -> models.py 에 작성할 때는 문자열로 적는 게 좋다.

# 방법 3. get_user_model 메서드
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 나의 유저 모델
        # model = settings.AUTH_USER_MODEL
        model = get_user_model()
        # fields = UserCreationForm.Meta.fields # Meta 상속이랑 같은 것
        # 회원가입이 하고 싶어요, 아래 내용을 입력받고 싶어요
        # 아무것도 안적으면 UserCreationForm 그대로 출력해버립니다.
        # fields = ''