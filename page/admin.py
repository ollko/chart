from django.contrib import admin


from .models import Loko, Filial, Mileage

class MileageAdmin(admin.ModelAdmin):
    model = Mileage
    list_display = ('id', 'filial', 'year', 'loko', 'mileage',)
    search_fields = ('filial__name', 'year',)
    ordering = ('id',)


admin.site.register(Mileage, MileageAdmin)

admin.site.register(Loko)


class FilialAdmin(admin.ModelAdmin):
    model = Filial
    list_display = ('id', 'name', 'slug',)
    search_fields = ('slug',)
    ordering = ('id',)

admin.site.register(Filial, FilialAdmin)


