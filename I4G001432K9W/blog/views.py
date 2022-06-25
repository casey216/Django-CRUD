from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy
 
class PostListView(ListView):
 
    # specify the model for list view
    model = Post

class PostCreateView(CreateView):
 
    # specify the model for create view
    model = Post

    # specify the field for create view
    fields = "__all__"

    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
 
    # specify the model for list view
    model = Post

class PostUpdateView(UpdateView):
 
    # specify the model for list view
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy('blog:all')

class PostDeleteView(UpdateView):
 
    # specify the model for list view
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy('blog:all')