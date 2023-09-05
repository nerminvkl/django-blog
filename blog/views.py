from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Clanak
from django.contrib.auth.models import User

def home(request):
    context = {
        'postovi': Clanak.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Clanak
    template_name = 'blog/home.html'
    context_object_name = 'postovi'
    ordering = ['-datum_objave']
    paginate_by = 4

class UserPostListView(ListView):
    model = Clanak
    template_name = 'blog/user_posts.html'
    context_object_name = 'postovi'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Clanak.objects.filter(autor=user).order_by('-datum_objave')


class PostDetailView(DetailView):
    model = Clanak
    
class PostCreateView(CreateView):
    model = Clanak
    fields = ['naslov', 'sadrzaj']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Clanak
    fields = ['naslov', 'sadrzaj']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Clanak
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'naslov': 'O aplikaciji'})

def contact(request):
    return render(request, 'blog/contact.html', {'naslov': 'Kontakt'})

def tail(request):
    return render(request, 'blog/tail.html', { 'naslov': 'Tailwind CSS'})

