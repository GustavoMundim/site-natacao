from django.contrib import admin
from .models import Inicio, Inscrito, Foto
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class IncricaoAjuste(resources.ModelResource):
    class Meta:
        model = Inscrito
        fields = ('nome', 'sobrenome', 'idade')


        


@admin.register(Inscrito)
class InscricaoView(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'idade')
    resource_class = IncricaoAjuste
    


@admin.register(Foto)
class FotoView(admin.ModelAdmin):
    list_display = ('icone', 'foto', 'data')


@admin.register(Inicio)
class InicioView(admin.ModelAdmin):
    list_display = ('imagem_wallpaper', 'titulo')
    list_editable = ('titulo',)

   





