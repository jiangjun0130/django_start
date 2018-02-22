from django.db import models

# Create your models here.

class UserMessage(models.Model):
    name = models.CharField( max_length=20)
    email = models.EmailField()
    address = models.CharField( max_length=100)
    message = models.CharField( max_length=500)

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name
        db_table = "user_message"