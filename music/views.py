from .models import Album,Song
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import authenticate,login
from .forms import UserForm

# Create your views here.

class IndexView(generic.ListView):
    template_name='music\index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model=Album
    template_name = 'music\details.html'

class Create_Song(CreateView):
    model = Song
    fields = ['song_title']

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


        #def favorite(request,album_id):
 #       album=get_object_or_404(Album,pk=album_id)
 #       try:
 #           selected_song=album.song_set.get(pk=request.POST['song'])
  #      except(KeyError,Song.DoesNotExist):
  #          return render(request,'music/details.html',{'album':album,'error_mssge':"You didnot select a valid song",})

   #     else:
   #         selected_song.is_favorite=True
   #         selected_song.save()
   #         return render(request,'music/details.html',{'album':album})




