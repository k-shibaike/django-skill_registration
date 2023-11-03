from django.urls import path
from . import views

app_name = "talent_search"

urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("user/<int:pk>", views.DetailView.as_view(), name="detail"),
]