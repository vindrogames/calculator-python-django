from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("suma/", views.suma, name="suma"),
    path("resta/", views.resta, name="resta"),
    path("mult/", views.mult, name="mult"),
    path("divide/", views.divide, name="divide"),
    path('ferjavascript/', TemplateView.as_view(template_name='calculator/fer_javascript.html')),
    path('maikjavascript/', TemplateView.as_view(template_name='calculator/maik_javascript.html')),
    path('ferhtmx/', TemplateView.as_view(template_name='calculator/fer_htmx.html')),
    path('clicked/', views.clicked, name="clicked"),
]