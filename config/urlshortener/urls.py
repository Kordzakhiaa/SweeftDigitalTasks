from django.urls import path

from urlshortener.views import RandomShortenedUrlView

app_name: str = 'url_shortener'

urlpatterns = [
    path('random_shorten/', RandomShortenedUrlView.as_view(), name='random_shortened_url'),
]
