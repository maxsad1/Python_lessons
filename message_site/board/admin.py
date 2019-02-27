from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_mail", "user",  "post_date")
    ordering = ("-post_date", )
    date_hierarchy = "post_date"
    list_filter = ("author_mail", )
    # fields = ("author_name", "author_mail", "post_date", "text")
    fieldsets = [("Author Info", {
        "fields": (
            "author_name",
            "author_mail",
            "user",
        )
    }), ("Date Info", {
        "fields": ("post_date", ),
        "classes": ("collapse", )
    }), ("Message Text", {
        "fields": ("text", )
    })]
    readonly_fields = ("post_date", )
