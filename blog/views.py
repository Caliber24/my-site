from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from website.models import Contact

from .models import Post
# Create your views here.

def blog_view(request, **kwargs):
  posts = Post.objects.filter(status=1)
  if kwargs.get('cat_name') != None:
    posts = posts.filter(category__name=kwargs['cat_name'])
  if kwargs.get('author_username') != None:
    posts = posts.filter(author__username=kwargs['author_username'])
  posts = Paginator(posts, 2)
  try:
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
  except PageNotAnInteger:  
    posts = posts.get_page(1)
  except EmptyPage:
    posts = posts.get_page(1)
  return render(request, "blog/blog-home.html", {'posts':posts})

def blog_single(request, id):
  posts = Post.objects.filter(status=1).order_by('-published_date')
  post = get_object_or_404(Post, pk=id, status=1)
  index = list(posts).index(post)
  next_post = None
  prev_post = None
  
  if index+1 < len(posts) and posts[index+1]:
    next_post = posts[index+1]
  

  posts = posts.reverse()
  index= (len(posts)-1)-index
  if index+1 < len(posts) and posts[index+1]:
    prev_post = posts[index+1]
  post.counted_view +=1
  post.save()
  context = {
    'post': post,
    'next': next_post,
    'prev': prev_post
  }
  return render(request, "blog/blog-single.html",context)

def blog_category(request, cat_name):
  posts = Post.objects.filter(status=1, category__name=cat_name)
  return render(request,'blog/blog-home.html', {'posts': posts})


def blog_search (request, **kwargs):
  posts = Post.objects.filter(status=1)
  # warlost
  if request.method == 'GET':
    if s := request.GET.get('s'):
      posts = posts.filter(content__contains=s)
  return render(request, "blog/blog-home.html", {'posts':posts})

