from django.contrib import admin
from . import models
# Register your models here.

# 注册所有需要的表
admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Music)
admin.site.register(models.Message)
admin.site.register(models.Visit)
admin.site.register(models.Tags)
admin.site.register(models.AboutAuthor)
admin.site.register(models.JobExperience)
