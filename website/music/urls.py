from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:album_id>/', views.detail, name="detail")
]
