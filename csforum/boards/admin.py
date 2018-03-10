from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.articleInfo)
admin.site.register(models.articleBody)
admin.site.register(models.users)


