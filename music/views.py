from .models import Album,Song
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate,login
from .forms import UserForm,AddSongForm

# Create your views here.

class IndexView(generic.ListView):
    template_name='music\index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class View_Songs(generic.ListView):
    template_name='music\disp_songs.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name = 'music\details.html'

class Create_Album(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class Update_Album(UpdateView):
    model=Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class Delete_Album(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('music:index')

        return render(request,self.template_name,{'form':form})


def fav_album(request,album_id):
    album=Album.objects.all()
    selected_album=get_object_or_404(Album,pk=album_id)
    if selected_album.album_is_fav:
        selected_album.album_is_fav=False
    else:
        selected_album.album_is_fav=True
    selected_album.save()
    return render(request,'music/index.html',{'all_albums':album})


def add_song(request,album_id=None):
    album=get_object_or_404(Album,pk=album_id)
    form=AddSongForm(request.POST or None)
    if form.is_valid():
        album_songs=album.song_set.all()
        for song in album_songs:
            if song.song_title==form.cleaned_data.get('song_title'):
                return render(request,'music/song_form.html',{'album':album,'form':form,'error_mssge':"You have already added that song"})

        added_song=form.save(commit=False)
        added_song.album=album
        added_song.save()
        return render(request, 'music/details.html', {'album': album})

    else:
        return render(request,'music/song_form.html',{'album':album,'form':form})

def delete_song(request,album_id,song_id):
    album=get_object_or_404(Album,pk=album_id)
    song_to_be_deleted=album.song_set.get(pk=song_id)
    song_to_be_deleted.delete()
    return render(request,'music/details.html',{'album':album})

def fav_song(request,album_id,song_id):
    album = get_object_or_404(Album, pk=album_id)
    selected_song= album.song_set.get(pk=song_id)
    if selected_song.song_is_fav:
        selected_song.song_is_fav=False
    else:
        selected_song.song_is_fav=True
    selected_song.save()
    return render(request, 'music/details.html', {'album': album})



