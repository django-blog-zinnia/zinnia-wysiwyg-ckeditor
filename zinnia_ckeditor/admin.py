"""EntryAdmin for zinnia-ckeditor"""
from django.contrib import admin

from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin


class EntryAdminCKEditorMixin(object):
    """
    Mixin adding CKEditor for editing Entry.content field.
    """
    pass


class EntryAdminCKEditor(EntryAdminCKEditorMixin,
                         EntryAdmin):
    """
    Enrich the default EntryAdmin with CKEditor.
    """
    pass

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdminCKEditor)
