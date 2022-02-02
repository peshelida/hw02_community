from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Group, Post


POSTS_LIMIT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:POSTS_LIMIT]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Это главная страница проекта Yatube'
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[
        :POSTS_LIMIT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
