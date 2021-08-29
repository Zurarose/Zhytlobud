from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Areas)
admin.site.register(Streets)
admin.site.register(Subways)
admin.site.register(Financing)
admin.site.register(Ownership)
admin.site.register(Customers)
admin.site.register(Buildings)
admin.site.register(Houses)
admin.site.register(Sections)
admin.site.register(SalesAndPrices)
admin.site.register(Logger)
admin.site.site_header = "Панель администратора серверной части приложения"


