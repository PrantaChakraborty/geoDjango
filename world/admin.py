from django.contrib.gis import admin

from .models import WorldBorder

admin.site.register(WorldBorder, admin.ModelAdmin)
# admin.site.register(WorldBorder, admin.GISModelAdmin)  # to show with street
