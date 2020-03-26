from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class HomeView(ListView):
    model = Article
    template_name = 'fit/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
       # context[""] = 
        return context
    
class ArticleView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context[""] = 
        return context
    
