from django.contrib import admin
from django.contrib import admin
# from .models import Buyer
from .models import *
admin.site.register(MService)
admin.site.register(MInstitutions)
admin.site.register(MStaatus)
admin.site.register(MAppointments)

# admin.site.register(Profile)

#
# @admin.register(Buyer)
# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'middle_name')

