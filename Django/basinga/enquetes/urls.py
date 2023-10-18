from django.urls import path
from . import views


# patterns significa padroes ou padrao
urlpatterns = [
    path("", views.index, name="index"),
]

#