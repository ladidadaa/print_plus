from django.contrib import admin
from .models import *


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'format', 'document', 'price')
    search_fields = ('format', 'document',)


admin.site.register(Documents, DocumentsAdmin)
