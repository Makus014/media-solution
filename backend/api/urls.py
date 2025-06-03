
from django.urls import path
from api.views.News.news import get_current_news
from api.views.Analyze.analyze import analyze_news


urlpatterns = [
    path('news/', get_current_news),
    path('analyze/', analyze_news)
]