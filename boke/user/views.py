from django.shortcuts import render

from .forms import RegisterForm
from .models import User


def login(request):

    return render(request,'login.html')


def register(request):
    form = RegisterForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            request.session['user'] = user
            return register('list_boke')
    user = User.objects.all().count()
    return render(request, 'register.html',{'form':form})


def user_info(request):
    return render(request,'user_info.html')