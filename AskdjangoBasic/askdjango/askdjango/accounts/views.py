from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignupForm

#로그인된 상활을 보장! 아니면 익명의 유저로 뜸
#로그아웃일 땐 settings.LOGIN.URL로 이등
@login_required 
def profile(request):
    return render(request, 'accounts/profile.html')

#방법1) 함수기반
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST) =>SignupForm
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)
#     else:
#         form = UserCreationForm() =>SignupForm
#     return render(request, 'accounts/signup.html', {
#         'form': form,
#     })

#방법2) 클래스기반
signup = CreateView.as_view(
    model=User,
    form_class=UserCreationForm,
    success_url=settings.LOGIN_URL,
    template_name="accounts/signup.html")
