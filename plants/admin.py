from django.contrib import admin

from .models import Plant, Propogation


class PropogationAdmin(admin.ModelAdmin):
    fields = ['plant', 'prop_location']


admin.site.register(Plant)
# admin.site.register(Propogation)
admin.site.register(PropogationAdmin)
