from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("workshop/", views.workshop, name="workshop"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact/", views.contact, name="contact"),
    path("registration/", views.registration, name="registration"),
    path("submit/", views.submit, name="submit"),
]
