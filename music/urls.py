from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [

    url(r'^login/$',views.login_user,name='user-login'),

    url(r'^logout/$',views.logout_user,name='user-logout'),

    url(r'^$', views.index, name='index'),

    # /music/songs/
    url(r'^songs/$',views.view_songs,name='display-songs'),

    url(r'^register/$',views.UserFormView.as_view(), name='register'),

    # /music/2/
    url(r'^(?P<album_id>[0-9]+)/$',views.view_details,name='detail'),

    # /music/2/fav_album/
    url(r'^(?P<album_id>[0-9]+)/fav_album/$', views.fav_album, name='fav-album'),

    # /music/2/newsong/
    url(r'^(?P<album_id>[0-9]+)/newsong/$',views.add_song,name='add-song'),

    # /music/2/delete/4/
    url(r'^(?P<album_id>[0-9]+)/delete/(?P<song_id>[0-9]+)/$',views.delete_song,name='delete-song'),

    # /music/2/fav_song/4/
    url(r'^(?P<album_id>[0-9]+)/fav_song/(?P<song_id>[0-9]+)/$', views.fav_song, name='fav-song'),

    # /music/album/add/
    url(r'^album/add/$',views.create_album,name='add-album'),

    # /music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$',views.Update_Album.as_view(),name='update-album'),

    # /music/2/delete/
    url(r'^album/(?P<album_id>[0-9]+)/delete/$',views.delete_album,name='delete-album'),

]
