from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$',views.UserFormView.as_view(), name='user-form'),

    # /music/2/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

    # /music/album/add/
    url(r'^album/add/$',views.Create_Album.as_view(),name='add-album'),

    # /music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$',views.Update_Album.as_view(),name='update-album'),

    # /music/2/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.Delete_Album.as_view(),name='delete-album'),

    # /music/album/
    #url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
]
