"""FSSocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('about', about, name='about'),
    path('changelog', changelog, name='changelog'),
    path('registration', registration, name='registration'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('id<profile_id>', profile, name='profile'),
    path('find', find, name='find'),
    path('iplogger', iplogger, name='iplogger'),
    path('', index, name='index'),
    #AJAX
    path('delete_post', delete_post, name='delete_post'),
    path('add_comment', add_comment, name='add_comment'),
    path('finder', finder, name='finder'),
    #socketio
    path('im', messages, name='messages')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()