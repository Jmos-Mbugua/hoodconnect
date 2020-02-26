from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from .models import Post, Profile, Business
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class ProfileView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profile.html'
    login_url = 'account_login'

class BusinessListView(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'businesses.html'
    login_url = 'account_login'


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Business
    context_object_name = 'post_list'
    template_name = 'businesses.html' 
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Business.objects.filter(Q(name__icontains=query))

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'account_login'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'upload_post.html'
    fields = '__all__'
    login_url = 'account_login'

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'hood', 'description', 'business', 'image']
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.user != self.request.user.username:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
