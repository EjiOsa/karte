from django.db import models
# Create your models here.

class Job(models.Model):
    """職種"""
    name = models.CharField(verbose_name = "職種名",max_length = 32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "職種"
        verbose_name_plural = "職種"

class Role(models.Model):
    """権限"""
    name = models.CharField(verbose_name = "権限名", max_length = 32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "役職"
        verbose_name_plural = "役職"

class Staff(models.Model):
    """職員"""
    name = models.CharField(max_length = 32)
    job = models.ForeignKey(Job, on_delete = models.PROTECT, verbose_name = "職種名")
    role = models.ForeignKey(Role, on_delete = models.PROTECT, verbose_name = "権限名")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "職員"
        verbose_name_plural = "職員"
