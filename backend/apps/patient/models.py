from django.db import models
from django.db.models.fields import json
from apps.staff.models import Staff
# Create your models here.

class Disease(models.Model):
    """疾患"""
    name = models.CharField(verbose_name = "疾患名", max_length = 128, unique = True)
    maker = models.ForeignKey(Staff,
                              on_delete = models.PROTECT,
                              verbose_name = "作成者",
                              limit_choices_to={"job": 1,} )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "疾患"
        verbose_name_plural = "疾患"

class Rest(models.Model):
    """安静度"""
    level = models.CharField(verbose_name = "安静度", max_length = 32,)
    maker = models.ForeignKey(Staff, on_delete = models.PROTECT, verbose_name = "作成者", )

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "安静度"
        verbose_name_plural = "安静度"

class Patient(models.Model):
    """患者"""
    name = models.CharField(verbose_name = "氏名", max_length=64)
    age = models.PositiveSmallIntegerField(verbose_name = "年齢",)
    level = models.ForeignKey(Rest, on_delete = models.PROTECT, verbose_name = "安静度")
    disease = models.ForeignKey(Disease, on_delete = models.PROTECT, verbose_name = "疾患名")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "患者"
        verbose_name_plural = "患者"