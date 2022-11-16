from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.BookCreateView.as_view(), name="book-create"),
]
