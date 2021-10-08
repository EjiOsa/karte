from django.db import models
from apps.master.models import Job, Role
# Create your models here.

class Staff(models.Model):
    SEX_MALE = "male"
    SEX_FEMALE = "female"
    SEX_SET = (
            (SEX_MALE, "男性"),
            (SEX_FEMALE, "女性"),
    )
    """職員"""
    last_name = models.CharField(verbose_name = "苗字", max_length=64, default=None,)
    first_name = models.CharField(verbose_name = "名前", max_length=64, default=None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length=64, default=None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length=64, default=None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default=None,)
    sex = models.CharField(verbose_name = "性別", choices=SEX_SET, default=None, max_length=8,)
    job = models.ForeignKey(Job, on_delete = models.PROTECT, verbose_name = "職種名", )
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名", )
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "職員"
        verbose_name_plural = "職員"
