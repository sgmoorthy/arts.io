from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/(?P<gallery_id>[0-9]+)/$', views.gallery, name='gallery'),
    url(r'^art_piece/(?P<art_id>[0-9]+)/$', views.art_piece, name='art'),
    url(r'^gallery/(?P<gallery_id>[0-9]+)/star/$', views.star_gallery, name='star_gallery'),
    url(r'^art_piece/(?P<art_id>[0-9]+)/star/$', views.star_art, name='star_art'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.signin, name='login'),
]
