from django.shortcuts import render,redirect
from django.core.cache import cache
from redis import Redis
from django.conf import settings
from app.models import Post


rds = Redis(**settings.REDIS)


def login_required(view_func):
    def check(request):
        user = request.session.get('user',None)
        if user:
            return view_func(request)
        else:
            return redirect('user:login')
    return check


def page_cache(timeout):
    def wrap1(view_func):
        def wrap2(request):
            key = 'PageCache-%s-%s'%(request.session.session_key, request.get_full_path())
            response = cache.get(key)
            if response is None:
                response = view_func(request)
                cache.set(key,response,timeout)
            return response
        return wrap2
    return wrap1


def read_count(read_view):
    def wrap(request):
        response = read_view(request)

        # 页面正常则进行阅读计数
        if response.status_code < 300:
            post_id = request.GET.get('post_id')
            rds.zincrby('ReadRank', post_id)

        return response
    return wrap


def get_top_n(num):
    '''获取阅读量前 N 的文章'''
    # ori_data = [
    #     (b'38', 321.0),
    #     (b'1', 239.0),
    #     (b'39', 111.0)
    #     ...
    # ]
    ori_data = rds.zrevrange(b'ReadRank', 0, num - 1, withscores=True)  # 取出原始排名数据

    # rank_data = [
    #    [1, 1035],
    #    [38, 687],
    #    [39, 214],
    # ]
    rank_data = [[int(post_id), int(count)] for post_id, count in ori_data]  # 数据清洗

    # 批量获取 post 对象
    post_id_list = [post_id for post_id, _ in rank_data]  # 取出每一个 post_id
    posts = Post.objects.filter(id__in=post_id_list)      # filter 的结果会按 id 生序排列
    posts = sorted(posts, key=lambda p: post_id_list.index(p.id))  # 重新整理成按 post_id_list 的顺序排列

    # 修改 rank_data 每一项的第一个元素为 post 对象
    # rank_data = [
    #     [<Post(1)>, 1035],
    #     [<Post(38)>, 687],
    #     [<Post(39)>, 214],
    #     ...
    # ]
    for item, post in zip(rank_data, posts):
        item[0] = post

    return rank_data
