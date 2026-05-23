from django.urls import path
from .views import AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView, PhotoCreateView

urlpatterns = [
    path('', AlbumListView.as_view(), name='album_list'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('create/', AlbumCreateView.as_view(), name='album_create'),
    path('<int:pk>/update/', AlbumUpdateView.as_view(), name='album_update'),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
    path('<int:album_id>/photos/add/', PhotoCreateView.as_view(), name='photo_add'),
]
