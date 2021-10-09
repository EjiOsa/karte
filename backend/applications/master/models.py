from django.db import models
from applications.const import JOB_SET

# Create your models here.

class Disease(models.Model):
    """疾患"""
    name_ja = models.CharField(verbose_name = "疾患名", max_length = 128, unique = True)
    name_en = models.CharField(verbose_name = "疾患名(英語)", max_length = 128, unique = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "疾患"
        verbose_name_plural = "疾患"

class Rest(models.Model):
    """安静度"""
    level = models.CharField(verbose_name = "安静度", max_length = 32, unique = True)
    area = models.CharField(verbose_name = "活動範囲", max_length = 128,)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "安静度"
        verbose_name_plural = "安静度"

class Role(models.Model):
    """権限"""
    name = models.CharField(verbose_name = "権限名", max_length = 32)
    target = models.CharField(verbose_name = "対象職種", choices = JOB_SET, max_length = 32)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "役職"
        verbose_name_plural = "役職"
