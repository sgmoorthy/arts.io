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
    context = {
        'title': 'Register',
        'error_messages': []
    }

    failed = False

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password_verify = request.POST['password_verify']

        if User.objects.filter(username=username).exists():
            context['error_messages'].append('Username already exists')
            failed = True
        if password != password_verify:
            context['error_messages'].append('Passwords do not match')
            failed = True
        else:
            # Create user
            new_user = User.objects.create_user(
                username,
                email,
                password,
                first_name=fname,
                last_name=lname
            )
            new_user.save()
            print('successfully created new user', username)

        if failed:
            return render(request, 'showcase/register.html', context)
    else:
        return render(request, 'showcase/register.html', context)

    return HttpResponseRedirect(reverse('showcase:index'))


def signin(request):
    context = {
        'title': 'Login',
        'error_messages': []
    }

    failed = False

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
                context['error_messages'].append('Your account has been disabled')
                failed = True
        else:
            # return an 'invalid login' error message
            context['error_messages'].append('Invalid username/password')
            failed = True

        if failed:
            return render(request, 'showcase/login.html', context)
    else:
        # show form
        return render(request, 'showcase/login.html', context)

    return HttpResponseRedirect(reverse('showcase:index'))
