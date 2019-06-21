from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:album_id>/', views.detail, name="detail")
]