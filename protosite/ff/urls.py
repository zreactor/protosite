from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'standard', views.index, name='index'),
    url(r'fapp', views.index, name='index'),
]
