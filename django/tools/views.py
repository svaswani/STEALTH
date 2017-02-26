from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from tools.models import Post
from tools.forms import PostForm
from django.http import HttpResponseRedirect

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
