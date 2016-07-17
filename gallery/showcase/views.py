from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import ArtPiece, Gallery


def index(request):
    latest_galleries = Gallery.objects.order_by('-pub_date')[:10]
    context = {'latest_galleries': latest_galleries}
    return render(request, 'showcase/index.html', context)

def gallery(request, gallery_id):
    p = get_object_or_404(Gallery, pk=gallery_id)
    return HttpResponse('Thanks for viewing gallery ' + str(gallery_id))

def art_piece(request, art_id):
    p = get_object_or_404(ArtPiece, pk=art_id)
    return HttpResponse('Thanks for viewing art piece ' + str(art_id))
