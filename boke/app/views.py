from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.db.models import Q

from .helper import save_post,fenye,Page_fenye
from .forms import ModelsForm
from .models import Comments


class List_boke(View):
    '''
    显示列表信息
    分页
    处理post请求的创建信息
    '''
    def get(self,request):
        data_all = Comments.objects.all()
        Page_fenye(data_all,4)
        page, page_all_num, page_number, page_list = fenye(request,data_all,4,3)
        context = {
            'page':page,
            'page_all_num':page_all_num,
            'page_number':page_number,
            'page_list':page_list,
        }
        return render(request,'bbs/post_list.html',context)

    def post(self,request):
        model_form = ModelsForm(request.POST)
        if model_form.is_valid():
            save_post(request)
        return redirect('list_boke')


class Cseate_boke(View):
    '''
    创建
    '''
    def get(self,request):
        return render(request,'bbs/create.html')




class update_boke(View):
    '''
    修改
    '''
    def get(self,request):
        tid = request.GET.get('post_id')

        data_all = Comments.objects.get(id=tid)
        context = {'data_all':data_all,'tid':tid}
        return render(request,'bbs/edit.html',context)
# 修改
def up_post(request,tid):
    model_form = ModelsForm(request.POST)
    if model_form.is_valid():
        save_post(request,tid)
    return redirect('list_boke')


class Detail_boke(View):
    '''
    阅读查看
    '''
    def get(self,request):
        tid = request.GET.get('post_id')
        data_all = Comments.objects.get(id=tid)
        context = {'data_all': data_all, 'tid': tid}
        return render(request, 'bbs/read.html', context)


class Search_boke(View):
    def post(self,request):
        content = request.POST.get('keyword', None)
        # print(content)
        # if content != None:
        #     request.session['content'] = content
        #     content = request.session.get('content')
        # if content == None:
        #     content = request.session.get('content')
        # print(content)
        data_all = Comments.objects.filter(Q(title__icontains=content) | Q(content__icontains=content))
        print(data_all)
        # page, page_all_num, page_number, page_list = fenye(request, data_all, 1, 2)
        #
        # context = {
        #     'page': page,
        #     'page_all_num': page_all_num,
        #     'page_number': page_number,
        #     'page_list': page_list,
        # }

        # p = Page_fenye(data_all, 2)
        # p.pages()
        # page_all_num = p.page_num()
        #
        # page_number = int(request.GET.get('page', 1))
        # print(page_number, '===========================')
        # page_list = []
        # if page_number + 3 <= page_all_num:
        #     for i in range(page_number, page_number + 3):
        #         page_list.append(i)
        # else:
        #     for i in range(page_number, page_all_num + 1):
        #         page_list.append(i)
        # page = p.page(page_number)
        context = {
            'data_all':data_all,
            # 'page': page,
            # 'page_all_num': page_all_num,
            # 'page_number': page_number,
            # 'page_list': page_list,
        }
        return render(request,'bbs/search.html',context)


