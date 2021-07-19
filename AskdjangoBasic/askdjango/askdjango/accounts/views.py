from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignupForm

#로그인된 상활을 보장! 아니면 익명의 유저로 뜸
#로그아웃일 땐 settings.LOGIN.URL로 이등
@login_required 
def profile(request):
    return render(request, 'accounts/profile.html')

# 방법1) 함수기반회원가입 + 후 자동로그인
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST) 
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user) #자동으로 로그인 처리
#             next_url=request.GET('next') or profile
#             return redirect(next_url) #로그인 됐으면 프로필화면으로
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     }

# 방법2) 클래스기반회원가입
# signup = CreateView.as_view(
#     model=User,
#     form_class=UserCreationForm,
#     success_url=settings.LOGIN_URL,
#     template_name="accounts/signup.html")

# 방법2) 클래스기반회원가입+ 후에 자동로그인
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next') or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())


signup = SignupView.as_view()