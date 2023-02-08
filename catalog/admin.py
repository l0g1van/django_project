from django.contrib import admin
from catalog.models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'date_time')

    fieldsets = [
        (None, {'fields': ['path', 'method']}),
        ('Date information', {'fields': ['date_time'], 'classes': ['collapse']}),
        ('Query and Body', {'fields': ['body', 'query'], 'classes': ['collapse']})
                 ]
    list_filter = ['date_time']
    search_fields = ['method', 'path']
