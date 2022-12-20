from django.contrib import admin

# Register your models here.
from .models import MyUUIDModel,Place,Todo,Test

admin.site.register(MyUUIDModel)
admin.site.register(Place)
admin.site.register(Todo)
admin.site.register(Test)

