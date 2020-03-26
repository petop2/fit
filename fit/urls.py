from django.urls import path
from .views import HomeView, ArticleView

app_name = 'fit'

urlpatterns = [
    path('', HomeView.as_view(), name='fit_list'),
    path('articles/',ArticleView.as_view(), name='articles')
]