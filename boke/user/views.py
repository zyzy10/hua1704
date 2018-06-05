
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
from urllib.parse import urlencode
from .forms import RegisterForm
from .models import User
from .helper import login_required


def login(request):
    querystring = urlencode(settings.AUTHORIZE_PARAMS)
    weibo_login_api = '%s?%s' % (settings.AUTHORIZE_API, querystring)
    users = User.objects.all()
    if request.method == 'POST':
        print('====post===')
        nlck = request.POST.get('nick')
        pssword = request.POST.get('pssword')
        print(nlck)
        print(pssword)
        try:
            user = User.objects.get(nlck=nlck)
        except User.DoesNotExist:
            return render(request,'login.html',{'error':'用户名错误','weibo_login_api': weibo_login_api})
        if check_password(pssword,user.pssword):
            request.session['user'] = user.nlck
            request.session['uid'] = user.id
            return redirect('user:user_info')
        return render(request, 'login.html', {'error': '密码错误','weibo_login_api': weibo_login_api})

    print('====get====')
    context = {
        'users':users,
        'weibo_login_api': weibo_login_api,
    }
    return render(request,'login.html',context)


def register(request):
    form = RegisterForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.pssword = make_password(user.pssword)
            user.save()
            request.session['user'] = user.nlck
            return redirect('user:user_info')
        else:
            return render(request,'register.html',{'error':form.errors})
    user = User.objects.all().count()
    return render(request, 'register.html',{'form':form})


@login_required
def user_info(request):
    nlck = request.session.get('user')
    nlck_name = User.objects.get(nlck=nlck)
    cntext = {
        'user':nlck_name,
    }
    return render(request,'user_info.html',cntext)


def logout(request):
    request.session.flush()
    return redirect('list_boke')

