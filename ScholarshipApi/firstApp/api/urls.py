from django.conf.urls import url
from .views import firstFunction


urlpatterns = [
    url('first', firstFunction)
]
