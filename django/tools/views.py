from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

from django.contrib.auth import logout

from django.conf import settings
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login as auth_login,
)
from django.contrib.auth.forms import (
    AuthenticationForm
)
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *

def index(request):
    return render(request, 'tools/index.html')

def detail(request, tool_id):
    post = get_object_or_404(Post, pk=tool_id)
    return render(request, 'tools/detail.html', {'tool': post})

def feed(request):
    posts = Post.objects.all()
    return render(request, 'tools/feed.html', {'posts': posts})

class CreateTool(CreateView):

    model = Post
    template_name = 'tools/post_form.html'

    form_class = PostForm

class EditTool(UpdateView):
    
    model = Post
    template_name = 'tools/post_form.html'

    form_class = PostForm


def login(request, template_name='tools/login.html',
              redirect_field_name=REDIRECT_FIELD_NAME,
              authentication_form=AuthenticationForm,
              current_app=None, extra_context=None):

    redirect_to = request.POST.get('redirect_field_name',
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return render(request, template_name, context)

def register(request):

    if request.method == 'POST':
        form = accountCreation( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return HttpResponseRedirect( '/' )
    else:
        form = accountCreation()

    return render( request, 'tools/register.html', {'form': form} )