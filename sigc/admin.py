from django.contrib import admin
from django.contrib.auth.models import Group, User
from sigc.models import *

# Register your models here.
@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'tipo']
    list_per_page = 10
    ordering = ('-nome', '-tipo',)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        list_display = ('nome', 'tipo', 'contato')
        return list_display

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    search_fields = ['setor', 'tipo']
    list_per_page = 10
    date_hierarchy = 'data_de_registro'
    ordering = ('-setor', '-tipo', '-situacao')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        return fieldsets

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        list_display = ('setor', 'data_de_registro', 'situacao', 'tipo')
        return list_display