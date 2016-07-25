from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import ArtPiece, Gallery
from .forms import RegisterForm, LoginForm


def index(request):
    latest_galleries = Gallery.objects.order_by('-pub_date')[:10]
    context = {
        'latest_galleries': latest_galleries,
        'title': 'New Galleries',
    }
    return render(request, 'showcase/index.html', context)

def gallery(request, gallery_id):
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    context = {
        'gallery': gallery,
        'title': gallery.name,
        'stars_range': range(int(gallery.rating)),
    }
    return render(request, 'showcase/gallery.html', context)

def art_piece(request, art_id):
    art_piece = get_object_or_404(ArtPiece, pk=art_id)
    context = {
        'image': art_piece,
        'title': art_piece.title,
    }
    return render(request, 'showcase/art.html', context)


def star_gallery(request, gallery_id):
    gal = get_object_or_404(Gallery, pk=gallery_id)
    gal.rating += 1
    gal.save()
    return HttpResponseRedirect(reverse('showcase:gallery', args=(gal.id,)))


def star_art(request, art_id):
    art = get_object_or_404(ArtPiece, pk=art_id)
    art.stars += 1
    art.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.method == 'POST':
        # create form instance
        form = RegisterForm(request.POST)

        # check if it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.cleaned_data['password'] != form.cleaned_data['password_verify']:
                return HttpResponseRedirect(reverse('showcase:register'))

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return HttpResponseRedirect(reverse('showcase:register'))

            # Create user
            new_user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
                first_name=form.cleaned_data['fname'],
                last_name=form.cleaned_data['lname']
            )
            new_user.save()

            # redirect to a new URL
            return HttpResponseRedirect(reverse('showcase:index'))
    else:
        # if a GET (or other method) create a blank form
        form = RegisterForm()

    return render(request, 'showcase/register.html', {'title': 'Register', 'form': form})


def signin(request):
    context = {
        'title': 'Login',

    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # redirect to a successful page
                print('successfully logged in')
            else:
                # Return a 'disabled account' error message
                print('account disabled')
        else:
            # return an 'invalid login' error message
            print('failed to login')
    else:
        # show form
        return render(request, 'showcase/login.html', context)

    return HttpResponseRedirect(reverse('showcase:index'))
