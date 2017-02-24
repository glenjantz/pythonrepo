from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^addtravel$', views.addtravel),
    url(r'^addtrip$', views.addtrip),
    url(r'^destination/(?P<id>\d+)$', views.destination),
    url(r'^jointrip/(?P<tripid>\d+)$', views.jointrip),
    url(r'^.+$', views.any)
]
