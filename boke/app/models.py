from django.db import models


class Comments(models.Model):
    title = models.CharField(max_length=40,verbose_name='标题')
    add_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True),
    create_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    content = models.TextField(verbose_name='内容')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'comments'