from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def logout_view(request):
    '''登出'''
    logout(request)
    return HttpResponseRedirect(reverse('demo_app:index'))


def register(request):
    '''注册'''
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用用户自动登录，再重定向到主页
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST['password1']
            )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('demo_app:index'))

    content = {'form': form}
    return render(request, 'users/register.html', content)
