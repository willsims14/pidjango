from django.contrib import admin

from .models import Plant, Propogation


class PlantAdmin(admin.ModelAdmin):
    # fields = ['common_name', 'scientific_name', 'description', 'image', 'slug']
    fieldsets = [

        (None,          {'fields': ['common_name', 'scientific_name', 'description',]}),
        ('Image & URL', {'fields': ['image', 'slug']}),
    ]


class PropogationAdmin(admin.ModelAdmin):
    fields = ['plant', 'prop_location']


admin.site.register(Plant, PlantAdmin)
admin.site.register(Propogation, PropogationAdmin)
