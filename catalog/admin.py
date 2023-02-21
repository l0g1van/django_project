from django.contrib import admin
from catalog.models import Logs, AuthorAndQuote


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


@admin.register(AuthorAndQuote)
class AuthorAndQuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'quote')

    fieldsets = [
        (None, {'fields': ['name', 'quote']}),
        ('Authors birth date', {'fields': ['birth_date']}),
        ('Author details', {'fields': ['details']})
    ]
