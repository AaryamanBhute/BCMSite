from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('portfolios', views.portfolios, name="portfolios"),
    path('investments', views.investments, name="investments"),
    path('about', views.about, name="about"),
    path('research', views.research, name="research")
]