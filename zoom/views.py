from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from user.models import User
from .form import PostForm, CommentForm
from .models import Post
# Create your views here.

@login_required(login_url='regis')
def index(request):
    posts = Post.objects.all().order_by('-pk')
    postss = request.GET.get('post', 1)
    #shu yerga paginatsiya qo'shish
    paginations = Paginator(post, 5)
    page_number = paginations.get_page(postss)
    print('\n\n', page_number, '\n\n')

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    ctx = {
        'posts': posts,
        'paginations': paginations
    }
    return render(request, 'site/index.html', ctx)


@login_required(login_url='regis')
def post(request):
    if request.POST:
        data = request.POST
        form = PostForm(data, request.FILES or None)
        if form.is_valid():
            form.user_id = request.user
            form.save()
        return redirect('add_post')

    return render(request, 'site/add_post.html')


@login_required(login_url='regis')
def author(request, user_id=None):
    users = User.objects.all().order_by('-pk')
    ctx = {
        'users': users
    }
    user_id = int(request.GET.get('user', request.user.id))
    posts = Post.objects.filter(user_id=user_id)
    ctx['posts'] = posts
    ctx['user_id'] = user_id
    return render(request, 'site/filter-author.html', ctx)