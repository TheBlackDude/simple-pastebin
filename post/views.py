from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


class HomeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/home.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_url'] = Post.objects.last()
        return context


class DetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    # Override the get_object method to lookup by random url
    def get_object(self):
        post_url = self.kwargs.get('post_url')
        obj = self.model.objects.filter(post_url=post_url)
        return obj.get()
