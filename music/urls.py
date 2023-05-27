from django.urls import path

from . import views

app_name="music"

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_up/sign_up/', views.sign_up, name='sign_up/sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('user_home/', views.user_home, name='user_home'),
    path('search/', views.search, name='search'),
    path('user_home/allsongs/', views.allsongs, name='allsongs'),
    path('latest/', views.latest, name='latest'),
    # path('my_playlist/', views.my_playlist, name='my_playlist'),
    path('favourite/', views.favourite, name='favourite'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('logout/', views.logout_view, name='logout'),
    # path('user_home', views.user_search, name='search'),
    path('user_home/index', views.index, name='user_home_index'),
    path('search/',views.user_search),
    path('music/', views.music, name='music'),


]