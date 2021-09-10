from django.contrib import admin

# Register your models here.
from demo_app.models import Topic, Entry


class EntryList(admin.ModelAdmin):
    list_display = ('id', 'topic', 'text', 'date_added')
    list_display_links = ('id', 'topic', 'text')


admin.site.register(Topic)
admin.site.register(Entry, EntryList)
