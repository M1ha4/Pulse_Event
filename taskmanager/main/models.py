from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    name = models.CharField("Название", max_length=200)
    eng_name = models.CharField("Название (англ.)", max_length=200, default="temp")
    category = models.CharField("Категория", max_length=100)
    short_description = models.TextField("Краткое описание", max_length=500)
    long_description = models.TextField("Длинное описание", blank=True)
    date_time = models.DateTimeField("Дата и время проведения")
    duration = models.DurationField("Продолжительность", blank=True, null=True)
    location = models.CharField("Место проведения", max_length=300)
    age_limit = models.PositiveIntegerField("Возрастное ограничение", default=0, blank=True, null=True)
    max_participants = models.PositiveIntegerField("Максимальное количество участников", blank=True, null=True)
    min_participants = models.PositiveIntegerField("Минимальное количество участников", blank=True, null=True)
    current_participants = models.PositiveIntegerField("Текущее количество участников", blank=True, null=True, default=0)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0)
    prime_points = models.PositiveIntegerField("Баллы прайма", blank=True, null=True)
    main_image = models.ImageField("Главное фото", upload_to="main_event_photo/")
    participants_list = models.TextField("Список участников", blank=True)
    slug = models.SlugField("Slug", unique=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            n = 2
            # гарантируем уникальность
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base}-{n}"
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def participants_count(self):
        if not self.participants_list.strip():
            return 0
        return len([p for p in self.participants_list.split(";") if p.strip()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

# Модель для дополнительных медиа
class EventMedia(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="media")
    media_file = models.FileField("Фото/видео", upload_to="event_media/")
    description = models.CharField("Описание", max_length=200, blank=True)

    def is_image(self):
        return str(self.media_file).lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))


    def __str__(self):
        return f"{self.event.name} - {self.media_file}"


class Participant(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="participants")
    name = models.CharField("Имя", max_length=200)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Электронная почта")

    def __str__(self):
        return f"{self.name} ({self.phone})"
