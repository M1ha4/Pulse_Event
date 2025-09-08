from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import RegistrationForm
from django.utils import timezone

def index(request):
    return render(request, 'main/index.html')


def calendar_event(request):
    now = timezone.now()

    # Праймовые события: score > 7
    prime_events = Event.objects.filter(
#        prime_points=7,
        date_time__gte=now  # только будущие события
    ).order_by('-prime_points', 'date_time')  # сортировка: сначала по баллам, потом по дате

    # Будущие события
    future_events = Event.objects.filter(
        date_time__gte=now
    ).order_by('date_time')

    # Прошедшие события
    past_events = Event.objects.filter(
        date_time__lt=now
    ).order_by('-date_time')

    context = {
        "prime_events": prime_events,
        "future_events": future_events,
        "past_events": past_events,
    }
    return render(request, "main/calendar_event.html", context)


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)

    participants = event.participants_list.split(";") if event.participants_list else []

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]

            # Добавляем в список участников
            participants.append(f"{name} ({phone}, {email})")
            event.participants_list = ";".join(participants)
            event.current_participants += 1
            event.save()

            return redirect("event_success", slug=event.slug)
    else:
        form = RegistrationForm()

    return render(request, "main/event_detail.html", {
        "event": event,
        "form": form,
        "participants": participants,   # ← передаём список в шаблон
    })

def event_success(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "main/event_success.html", {"event": event})


def category_events(request, category_name):
    # Фильтруем события по категории и сортируем по дате
    events = Event.objects.filter(category=category_name).order_by('date_time')
    return render(request, 'main/category_events.html', {
        'events': events,
        'category_name': category_name
    })