from django.urls import path

from .views import HomeView, DetailView, DeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<str:post_url>', DetailView.as_view(), name='detail'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]
