from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/(?P<gallery_id>[0-9]+)/$', views.gallery, name='gallery'),
    url(r'^art_piece/(?P<art_id>[0-9]+)/$', views.art_piece, name='art_piece'),
]
