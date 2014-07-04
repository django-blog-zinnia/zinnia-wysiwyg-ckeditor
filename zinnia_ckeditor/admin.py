"""EntryAdmin for zinnia-ckeditor"""
from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget

from zinnia.models import Entry
from zinnia.admin.entry import EntryAdmin
from zinnia.admin.forms import EntryAdminForm


class EntryAdminCKEditorForm(EntryAdminForm):
    """
    Define the CKEditor widget for the content field.
    """
    content = forms.CharField(widget=CKEditorWidget())


class EntryAdminCKEditorMixin(object):
    """
    Mixin adding CKEditor for editing Entry.content field.
    """
    form = EntryAdminCKEditorForm


class EntryAdminCKEditor(EntryAdminCKEditorMixin,
                         EntryAdmin):
    """
    Enrich the default EntryAdmin with CKEditor.
    """
    pass

admin.site.unregister(Entry)
admin.site.register(Entry, EntryAdminCKEditor)
