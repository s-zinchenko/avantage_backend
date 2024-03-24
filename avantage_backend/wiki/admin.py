from django.contrib import admin

from avantage_backend.wiki.models import Letter, Record


class RecordInlineAdmin(admin.TabularInline):
    model = Record


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    inlines = [
        RecordInlineAdmin,
    ]


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
