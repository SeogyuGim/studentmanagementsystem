from django.contrib import admin
from .models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_datetime', 'updated_datetime',)
    search_fields = ('name',)


admin.site.register(Certificate, CertificateAdmin)
