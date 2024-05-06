from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("view", views.view, name="view"),
    path("add", views.add, name="add"),
    path("filter", views.filter, name="filter"),
    path("remove/<int:emp_id>", views.remove, name="remove"), # type: ignore
]
