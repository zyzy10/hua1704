from .models import Comments


def save_post(request,tid=0):
    title = request.POST.get('title')
    content = request.POST.get('content')

    if tid != 0:
        c = Comments.objects.get(pk=tid)
        c.title = title
        c.content = content
        c.save()
        print('aaaaaaaa')
    else:
        c = Comments()
        c.title = title
        c.content = content
        c.save()
        print('bbbbbbbb')


class Page_fenye(object):
    def __init__(self,data,num):
        self.data = data
        self.num = num

    def pages(self):
        data_dict = {}
        self.page_page1 = len(self.data) // self.num
        self.page_page2 = len(self.data) % self.num
        count = 0
        for i in range(self.page_page1):
            data_dict[i+1] = self.data[count:count+self.num]
            count += self.num
        if self.page_page2:
            for i in range(self.page_page2):
                data_dict[self.page_page1 + 1] = self.data[self.page_page1*self.num:]
        return data_dict

    def page_num(self):
        page = self.page_page1+self.page_page2
        return page


    def page(self,num):
        pages = self.pages()
        return pages[num]


def fenye(request,data_all,num,page_count):
    p = Page_fenye(data_all, num)
    p.pages()
    page_all_num = p.page_num()

    page_number = int(request.GET.get('page', 1))
    page_list = []
    if page_number + page_count <= page_all_num:
        for i in range(page_number, page_number + page_count):
            page_list.append(i)
    else:
        for i in range(page_number, page_all_num + 1):
            page_list.append(i)
    page = p.page(page_number)
    return page,page_all_num,page_number,page_list




    # content = request.POST.get('content',None)
    # if content != None:
    #     request.session['content'] = content
    #     content = request.session.get('content')
    # if content == None:
    #     content = request.session.get('content')
    # print(content)
    # data_all = Comments.objects.filter(Q(title__icontains=content)|Q(context__icontains=content))
    # p = Page_fenye(data_all, 2)
    # p.pages()
    # page_num = p.page_num()
    #
    # page_number = int(request.GET.get('page',1))
    # page_list = []
    # if page_number + 3 <= page_num:
    #     for i in range(page_number,page_number+3):
    #         page_list.append(i)
    # else:
    #     for i in range(page_number,page_num+1):
    #         page_list.append(i)
    #
    # page = p.page(page_number)
    # context = {
    #     # 'data_all':data_all,
    #     'page': page,
    #     'page_num': page_num,
    #     'page_list':page_list,
    #     'page_number':page_number,
    #     'search': 'search',
    # }