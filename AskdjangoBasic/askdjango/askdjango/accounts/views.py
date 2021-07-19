from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required 
#로그인된 상활을 보장! 아니면 익명의 유저로 뜸
#로그아웃일 땐 settings.LOGIN.URL로 이등
def profile(request):
    return render(request, 'accounts/profile.html')