from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.blog_view, name="blog-home"),
    path("<int:id>", views.blog_single, name="blog-single"),
    path("category/<str:cat_name>", views.blog_view, name="category"),
    path("search/", views.blog_search, name="search"),
    path("author/<str:author_username>", views.blog_view, name="author"),
]
