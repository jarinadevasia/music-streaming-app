from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# from django.core.paginator import paginator
def index(request):
    songs = Song.objects.all().order_by('-id')[:5]
    details = {'song': songs}
    return render(request, 'index.html', details)

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        conform_password = request.POST.get('conform_password', None)

        # Check if any of the required fields is missing
        if None in [username, email, password, conform_password]:
            messages.error(request, 'Please fill all the required fields')
            return redirect('sign_up/')

        # Check if username already exists
        if Registration.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
            return redirect('sign_up/')
        
        # Check if email already exists
        if Registration.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken')
            return redirect('sign_up/')

        # Check if password and confirm_password match
        if password != conform_password:
            messages.error(request, 'Passwords do not match')
            return redirect('sign_up/')

        # Create user
        user = Registration.objects.create(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('http://127.0.0.1:8000/sign_in/')
    else:
        return render(request, 'sign_up.html')

def sign_in(request):
    if request.method == 'POST':
        # Get the submitted credentials
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print(username)
        print(password)

        # Store the credentials in the database
        u = Registration.objects.filter(username=username, password=password)
        if u:
            request.session["id"]=u[0].id
            print("in")
            return redirect("http://127.0.0.1:8000/user_home/")
        else:
            print("not in")
            return render(request, 'sign_in.html',{'msg':"Incorrect username or password"})

        # Render a success page
        
    # Render the login form
    return render(request, 'sign_in.html')

def user_home(request):
    u= Registration.objects.filter(id= request.session["id"])

    if request.method == 'POST':
        item_search = request.POST.get('title')
        song = Song.objects.filter(title__icontains=item_search)
        context1 = {'song': song}
        return render(request, 'search.html', context1)

    context = {'user': u}
    return render(request, 'user_home.html', context)

# def allsongs(request):
#     songs = Song.objects.all().order_by('-id')
#     context = {'song': songs}
#     return render(request, 'allsongs.html', context)

def allsongs(request):
    songs = Song.objects.all().order_by('title')
    context = {'song': songs}
    return render(request, 'allsongs.html', context)

def search(request):
    return render(request, 'search.html')

def latest(request):
    songs = Song.objects.all().order_by('-id')[:5]
    details = {'song': songs}
    return render(request, 'latest.html', details)

def favourite(request):
    return render(request, 'favourite.html')
    
def my_profile(request):
    # id = request.GET.get('id')
    r = Registration.objects.filter(id=request.session["id"])
    context = {'profile': r}
    return render(request, 'my_profile.html', context)

def updateprofile(request):
    return render(request, 'updateprofile.html')

def updateprofile(request):
    if request.method == 'POST':
        username = request.session['id']
        up = Registration.objects.get(id=username)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        up.username = username
        up.password = password
        up.email = email
        up.save()
        r = Registration.objects.filter(id=request.session["id"])
        context = {'profile': r}
        return render(request, 'my_profile.html', context)

    else:
        id= request.GET.get('id')
        up = Registration.objects.get(id=id)
        context= {'up':up}
        return render(request, 'updateprofile.html', context)


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out successfully')
    return redirect('/') # assuming your index URL has the name 'index'

def user_search(request):
    title = request.GET.get('title')
    a = Song.objects.filter(title__icontains=title)
    return render(request, 'search.html', {'song': a})

def music(request):
    songs = Song.objects.all()
    details = {'song': songs}
    return render(request, 'music.html', details)

from django.shortcuts import get_object_or_404
def add_to_favorites(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if 'id' in request.session:
        user_id = request.session['id']
        if song.fav.filter(id=user_id).exists():
            message = "Already exists"
        else:
            song.fav.add(user_id)
            message = "song added to favorites."
    else:
        messages.error(request, message)
        return redirect('login') 
    
    favorites = Song.objects.filter(fav=user_id)
    context = {'message': message, 'favorites': favorites}
    return render(request, 'favorites.html', context)

#Remove Fav
def remove_from_fav(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if 'id' in request.session:
        user_id=request.session['id']
        if song.fav.filter(id=user_id).exists():
            song.fav.remove(user_id)
            message="song Removed From Favourites"
        else:
            messages="No song in Favourites"
    else:
        message = "You need to be logged in to add videos to favorites."
        messages.error(request, message)
        return redirect('login') 
    
    context = {'message': message}
    return render(request, 'home.html', context)
    



def favorites_list(request):
    if 'id' in request.session:
        user_id = request.session['id']
        favorites = Song.objects.filter(fav=user_id)
        return render(request, 'favourite.html', {'favorites': favorites})
    else:
        return render(request, 'favourite.html', {'favorites': None})