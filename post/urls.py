from django.urls import path

from .views import HomeView, DetailView, DeleteView, ListPostsView, PostVisits

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('list/', ListPostsView.as_view(), name='list'),
    path('<str:post_url>', DetailView.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('visits/<str:post_url>', PostVisits.as_view(), name='visits'),
]
