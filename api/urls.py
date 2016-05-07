from django.conf.urls import url, include
from . import views
from .views import IndexView, GreetView, JsonView, ColorView, ColorsView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^index/$', views.prueba),
    url(r'greet/([a-z]+)/$', csrf_exempt(GreetView.as_view())),
    url(r'json/$', csrf_exempt(JsonView.as_view())),
    url(r'color/([a-z]+)$', csrf_exempt(ColorView.as_view())),
    url(r'colors/$', ColorsView.as_view()),
]


