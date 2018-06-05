from django.shortcuts import render,redirect


def login_required(view_func):
    def check(request):
        user = request.session.get('user',None)
        if user:
            return view_func(request)
        else:
            return redirect('user:login')
    return check

