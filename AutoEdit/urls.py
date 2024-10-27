from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("editing_page/", views.editing_page, name='editing_page'),
    path("accounts/", include('django.contrib.auth.urls'))
]