from django.contrib import admin
from django.utils.html import format_html
from .models import Event, EventMedia

class EventMediaInline(admin.TabularInline):
    model = EventMedia
    extra = 1
    readonly_fields = ("preview_media",)

    def preview_media(self, obj):
        if obj.media_file:
            url = obj.media_file.url
            ext = url.split('.')[-1].lower()
            if ext in ['jpg', 'jpeg', 'png', 'gif']:
                return format_html('<img src="{}" style="height: 60px; margin-right: 5px;"/>', url)
            else:
                return format_html('<a href="{}" target="_blank">Файл</a>', url)
        return "-"
    preview_media.short_description = "Превью"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "eng_name",
        "category",
        "date_time",
        "location",
        "price",
        "current_participants",
        "max_participants",
        "prime_points",
        "preview_main_image",
    )
    search_fields = ("name", "na_angl", "category", "location")
    list_filter = ("category", "date_time")
    readonly_fields = ("preview_main_image",)
    inlines = [EventMediaInline]  # Подключаем галерею

    def preview_main_image(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="height: 60px;"/>', obj.main_image.url)
        return "-"
    preview_main_image.short_description = "Главное фото"
