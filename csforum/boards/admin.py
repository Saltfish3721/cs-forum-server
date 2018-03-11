from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.article)
admin.site.register(models.users)


