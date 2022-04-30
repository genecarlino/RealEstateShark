from audioop import add
from django.contrib import admin
from .models import (Leasing_Info, Address, UnitType, Community, Unit)

admin.site.register(Leasing_Info)
admin.site.register(Address)
admin.site.register(UnitType)
admin.site.register(Community)
admin.site.register(Unit)
# Register your models here.
