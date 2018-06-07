from django.db import models
from user.models import User


class Post(models.Model):
    uid = models.IntegerField(default=10)
    title = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        db_table = 'post'

    @property
    def user(self):
        if not hasattr(self, '_user_id'):
            self._user_id = User.objects.get(id=self.uid)
        return self._user_id


