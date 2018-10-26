from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Log
from .forms import PostForm


class HomeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/home.html'
    success_url = reverse_lazy('home')
    success_message = 'Post was created successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_url'] = Post.objects.last()
        return context


class ListPostsView(ListView):
    model = Post
    template_name = 'post/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('expiry_date')


class DetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    # Override the get_object method to lookup by random url
    def get_object(self):
        post_url = self.kwargs.get('post_url')
        # Log user info
        Log.objects.create(user_agent=self.request.META.get('HTTP_USER_AGENT'),
                           http_cookie=self.request.META.get('HTTP_COOKIE'),
                           remote_addr=self.request.META.get('REMOTE_ADDR'),
                           server_name=self.request.META.get('SERVER_NAME'),
                           post_url=post_url)
        obj = self.model.objects.filter(post_url=post_url)
        return obj.get()


class DeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    success_message = 'Post was deleted successfully'


class PostVisits(ListView):
    model = Log
    template_name = 'post/visits.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        post_url = self.kwargs.get('post_url')
        return queryset.filter(post_url=post_url)
