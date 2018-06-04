from math import ceil

from django.shortcuts import render,redirect
from .models import Post


def list_boke(request):
    page = int(request.GET.get('page', 1))  # 当前页码，默认为 1

    per_page = 2
    # 计算总页数
    total = Post.objects.count()
    pages = ceil(total / per_page)

    # 取出本页需要现实的文章
    '''
    start=0:0和2-1
    start=2:2和4-1
    start=4:4和6-1
    '''
    start = (page - 1) * per_page
    print(start,'======')
    end = start + per_page
    posts = Post.objects.all()[start:end]
    context = {
        'posts': posts,
        'pages': range(pages),
    }
    return render(request,'post_list.html',context)


def edit_boke(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('list_boke')
    post_id = request.GET.get('post_id')
    posts = Post.objects.get(id=post_id)
    context = {
        'post': posts,
    }
    return render(request,'edit.html',context)


def read_boke(request):
    page_id = request.GET.get('post_id')
    posts = Post.objects.get(id=page_id)
    context = {
        'post': posts,
    }
    return render(request,'read.html',context)


def create_boke(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('list_boke')
    return render(request,'create.html')


def search_boke(request):
    return render(request,'search.html')