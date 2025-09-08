from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import RegistrationForm

def index(request):
    return render(request, 'main/index.html')


def calendar_event(request):
    return render(request, 'main/Calendar_event.html')


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