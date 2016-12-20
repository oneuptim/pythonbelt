from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_process$' , views.register_process),
    url(r'^login_process$' , views.login_process),
    url(r'^success$', views.success),
    url(r'^poke/(?P<id>\d+)$', views.poke),
    # url(r'^add_quote$', views.add_quote),
    # url(r'^add_fav/(?P<id>\d+)$', views.add_fav),
    # url(r'^remove_fav/(?P<id>\d+)$', views.remove_fav),
    # url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^logout$', views.logout),
]
