from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album, Photo

class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'

class AlbumDetailView(LoginRequiredMixin, DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album_list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.owner or self.request.user.groups.filter(name="AlbumAdmin").exists()

class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album_list')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.owner or self.request.user.groups.filter(name="AlbumAdmin").exists()

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image']
    template_name = 'albums/photo_form.html'

    def form_valid(self, form):
        form.instance.album_id = self.kwargs['album_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album_detail', kwargs={'pk': self.kwargs['album_id']})