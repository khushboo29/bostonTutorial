from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]