from django.conf.urls import url
from . import views

app_name = 'service'

urlpatterns = [
    url(r'^chess/', views.chess, name='chess')
]
