from django.conf.urls import include, url
from .views import webhook

urlpatterns = [
    url(r'^webhook/?$', webhook)
]
