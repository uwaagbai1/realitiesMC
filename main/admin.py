from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from main.models import Project, MasterClass

admin.site.register((Project))

class MasterClassAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(MasterClass, MasterClassAdmin)