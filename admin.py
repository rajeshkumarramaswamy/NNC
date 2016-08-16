from django.contrib import admin
from dashboard.models import *


class NocAdmin(admin.ModelAdmin):
    model = Noc
    list_display = ('name',)


class PartnerAdmin(admin.ModelAdmin):
    model = Partner
    list_display = ('name', 'noc',)


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('name', 'partner', 'noc')


admin.site.register(Noc, NocAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Client, ClientAdmin)
