from django.db import models
from apps.master.models import Role
# Create your models here.
"""性別"""
SEX_MALE = "male"
SEX_FEMALE = "female"
SEX_SET = (
        (SEX_MALE, "男性"),
        (SEX_FEMALE, "女性"),
)
class Doctor(models.Model):
    """医師"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名",
                             limit_choices_to = {"target" : "DOCTOR"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "医師"
        verbose_name_plural = "医師"

class Nurse(models.Model):
    """看護師"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名", 
                             limit_choices_to = {"target" : "NURSE"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "看護師"
        verbose_name_plural = "看護師"

class Pharmacist(models.Model):
    """薬剤師"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名",
                             limit_choices_to = {"target" : "PHARMACIST"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "薬剤師"
        verbose_name_plural = "薬剤師"

class Physical(models.Model):
    """理学療法士"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名",
                             limit_choices_to = {"target" : "PHYSICAL"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "理学療法士"
        verbose_name_plural = "理学療法士"

class Occupational(models.Model):
    """作業療法士"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名",
                             limit_choices_to = {"target" : "OCCUPATIONAL"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "作業療法士"
        verbose_name_plural = "作業療法士"

class Clerk(models.Model):
    """事務職"""
    last_name = models.CharField(verbose_name = "苗字", max_length = 64, default = None,)
    first_name = models.CharField(verbose_name = "名前", max_length = 64, default = None,)
    last_name_kana = models.CharField(verbose_name = "みょうじ", max_length = 64, default = None,)
    first_name_kana = models.CharField(verbose_name = "なまえ", max_length = 64, default = None,)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",  default = None,)
    sex = models.CharField(verbose_name = "性別", choices = SEX_SET, max_length = 8,)
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名",
                             limit_choices_to = {"target" : "CLERK"})
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "事務員"
        verbose_name_plural = "事務員"