from django.urls import path
from . views import *


urlpatterns = [
    path('', home, name='home'),
    path('create_post/', create_post, name='create_post'),
    path('post/<slug:slug>/', detail, name='detail'),
    path('post_edit/<slug:slug>/', post_edit, name='post_edit'),
    path('post_delete/<slug:slug>/', post_delete, name='post_delete'),

    path('category/<slug:slug>/', category, name='category'),
    path('', contact, name='contact'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]