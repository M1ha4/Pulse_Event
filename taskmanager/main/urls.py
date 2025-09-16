from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('calendar/', views.calendar_event, name='calendar'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path("event/<slug:slug>/success/", views.event_success, name="event_success"),
    path('category/<str:category_name>/', views.category_events, name='category_events'),
    path('catering', views.catering, name='catering')
]
