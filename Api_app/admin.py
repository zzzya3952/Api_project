from django.contrib import admin

# Register your models here.

from Api_app.models import *

admin.site.register(DB_notice)
admin.site.register(DB_news)
admin.site.register(DB_project_list)
