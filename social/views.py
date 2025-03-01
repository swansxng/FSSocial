import uuid, os, json

from random import randint
from django.db.models import F
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.mail import send_mail
from .models import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

def about(request):
    response = render(request, 'social/about.html')
    return response

def changelog(request):
    return render(request, 'social/changelog.html')

def session_check(request):
    if 'profile_id' not in request.session:
        request.session['profile_id'] = 0
        request.session['profile_name'] = 'Anonimous'
        request.session['profile_surname'] = 'User'

def index(request):
    if 'profile_id' in request.session and request.session['profile_id'] != 0:
        return redirect(f'/id{request.session["profile_id"]}')
    return redirect('/login')

def registration(request):
    if request.method == 'POST':
        data = request.POST
        if 'email' in data:
            response = render(request, 'social/reg_code.html')
            response.set_cookie('email', data['email'])
            response.set_cookie('password', data['password']) # Не помню зачем это сделал но надо пофиксить
            response.set_cookie('name', data['name'])
            response.set_cookie('surname', data['surname'])
            code = str(randint(100000, 999999))
            send_mail(f'FSSocial - registration code [{code}]', code,
                      'mailto.fssocial@gmail.com', [data['email']], fail_silently=False)
            request.session['registration_code'] = code
            return response
        else:
            code = data['code']
            cookie_data = request.COOKIES
            if code == request.session['registration_code']:
                del request.session['registration_code']
                u = Users(email=cookie_data['email'],
                          password=cookie_data['password'],
                          name=cookie_data['name'],
                          surname=cookie_data['surname'])
                u.save()
                ure = Users.objects.get(email=cookie_data['email'])
                request.session['profile_id'] = ure.pk
                request.session['profile_name'] = ure.name
                request.session['profile_surname'] = ure.surname
                response = redirect(f'/id{ure.pk}')
                response.delete_cookie('email')
                response.delete_cookie('password')
                response.delete_cookie('name')
                response.delete_cookie('surname')
                return response

    return render(request, 'social/reg.html')

def login(request):
    if request.method == 'POST':
        data = request.POST
        user = Users.objects.get(email=data['email'])
        if data['password'] == user.password:
            request.session['profile_id'] = user.pk
            request.session['profile_name'] = user.name
            request.session['profile_surname'] = user.surname
            return redirect(f'/id{user.pk}')
    return render(request, 'social/login.html')

def logout(request):
    del request.session['profile_id']
    return redirect('/login')

def profile(request, profile_id):
    if request.method == 'POST':
        # create post
        data = request.POST
        if 'photo' in request.FILES:
            photo = request.FILES['photo']
            filename = str(uuid.uuid4()) + ".jpg"
            FileSystemStorage(location='static/social/usermedia/profiles/posts/').save(filename, photo)
        else:
            filename = None
        post = Post(posttext=data['posttext'],
                    image=filename,
                    post_id=Users.objects.get(id=request.session['profile_id']).post_count + 1,
                    owner_id=request.session['profile_id'])
        post.save()
        Users.objects.filter(id=request.session['profile_id']).update(post_count=F('post_count') + 1)
        data['posttext']
        return redirect(f'/id{request.session["profile_id"]}')
    session_check(request) # fix 500 error if you are not logged and in this point give you id0
    try:
        info = Users.objects.get(id=profile_id)
    except ObjectDoesNotExist:
        return render(request, 'social/404.html')
    posts = Post.objects.filter(owner_id=profile_id).order_by('-post_id')
    return render(request, 'social/profile.html', {'title':f'{info.name} {info.surname}',
                                                   'posts': posts,
                                                   'session_id': request.session['profile_id'],
                                                   'profile_id': info.id,
                                                   'session_name': f"{request.session['profile_name']} {request.session['profile_surname']}"})

def handler403(request, exception):
    return render(request, 'social/403.html')

def handler404(request, exception):
    return render(request, 'social/404.html')


def handler500(request):
    return render(request, 'social/500.html')

def delete_post(request):
    """
    TODO !No functional to delete user's image
    """
    if request.headers['X-Requested-With'] == 'XMLHttpRequest':
        if request.method == 'POST':
            data = json.load(request)
            Post.objects.get(post_id=data['post_id'],
                             owner_id=request.session['profile_id']).delete()
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def add_comment(request):
    if request.headers['X-Requested-With'] == 'XMLHttpRequest':
        if request.method == 'POST':
            data = json.load(request)
            post = Post.objects.get(post_id=data['post_id'],
                                    owner_id=data['profile_id'])
            comment = Comments(commenttext=data['comment'],
                               comment_id=post.comments_set.count() + 1,
                               post_id=post.id,
                               owner_id=request.session['profile_id'],
                               owner_name=f"{request.session['profile_name']} {request.session['profile_surname']}")
            comment.save()
            return HttpResponce('ok')
    else:
        return HttpResponseBadRequest('Invalid request')

def finder(request):
    if request.headers['X-Requested-With'] == 'XMLHttpRequest':
        if request.method == 'POST':
            data = json.load(request)
            if data['request'] == '':
                return JsonResponse(json.dumps([]), safe=False)
            users = Users.objects.filter(name__icontains=data['request']).values('id', 'name', 'surname')
            to_send = list(users)
            return JsonResponse(json.dumps(to_send), safe=False)
        else:
            return handler404()
def find(request):
    """social/find"""
    return render(request, 'social/find.html')

def messages(request):
    iplogger(request)
    return render(request, 'social/messages.html')

def iplogger(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return render(request, 'social/iplogger.html')