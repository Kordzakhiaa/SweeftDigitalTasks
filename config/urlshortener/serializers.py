from rest_framework import serializers

from urlshortener.models import UrlShortener
from urlshortener.validators import validate_url


class UrlRandomShortenerSerializer(serializers.ModelSerializer):
    original_url = serializers.URLField(validators=[validate_url], max_length=250)

    class Meta:
        model = UrlShortener
        fields = ['original_url']
