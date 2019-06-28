from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# commenting or discarding this file coz we are about to use Generic Views 
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request, 'music/index.html', context)


# Commenting this code as it is using loder and rewiting this function with render
# from django.template import loader
# from django.http import HttpResponse
# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums' : all_albums,
#     }
#     return HttpResponse(template.render(context, request))


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, 'Song.DoesNotExist'):
        return render(request, 'music/detail.html', {
            'album' : album,
            'error_message' : "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album':album})
