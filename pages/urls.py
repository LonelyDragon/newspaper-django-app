from django.urls import path
from django.urls.conf import include


from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]