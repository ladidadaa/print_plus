from django.contrib import admin
from .models import *


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'format', 'document', 'price')
    search_fields = ('format', 'document',)
    list_editable = ('type', 'format', 'document', 'price')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'paper_type', 'format', 'document_type', 'page_count', 'instance_count', 'price', 'file')
    search_fields = ('customer',)


admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Orders, OrdersAdmin)
