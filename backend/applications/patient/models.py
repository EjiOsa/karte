from django.db import models
from applications.master.models import Rest,Disease
from applications.const import SEX_SET,SEX_UNKNOWN
# Create your models here.

class Patient(models.Model):
    """患者"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, default = SEX_UNKNOWN, max_length = 8,)
    level = models.ForeignKey(Rest, on_delete = models.PROTECT, verbose_name = "安静度")
    disease = models.ForeignKey(Disease, on_delete = models.PROTECT, verbose_name = "疾患名")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{ self.last_name } {self.first_name }"

    class Meta:
        verbose_name = "患者"
        verbose_name_plural = "患者"