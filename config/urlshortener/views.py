from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from urlshortener.serializers import UrlRandomShortenerSerializer, UrlPremiumClientShortenerSerializer
from urlshortener.models import UrlShortener
from urlshortener.permissions import IsPremiumClient
from urlshortener.shortener import url_shortening


class RandomShortenedUrlView(APIView):
    """
    Endpoint that generating urls with random string
    ---------------------------------------------------------------------------------------------
    THIS ENDPOINT CAN BE USED BY BOTH ANONYMOUS AND AUTHENTICATED USERS(admins, premium_users...)
    BUT IF YOU WANT TO CREATE CUSTOM SHORT URL YOU MUST BE ADMIN OR PREMIUM USER AT ENDPOINT:
    .../premium/create_url/
    ---------------------------------------------------------------------------------------------
    """

    def get(self, request, *args, **kwargs) -> 'Response':  # noqa
        """
        :return -> {"is_premium_client": true}
                    if request.user is premium client
                    otherwise {"is_premium_client": false}
        """
        return Response({'is_premium_client': request.user.is_premium_client})

    def post(self, request, *args, **kwargs) -> 'Response':  # noqa
        """
        :Requesting original url (for example https://github.com/Kordzakhiaa)
        :Generating short url (for example http://127.0.0.1:8000/IYFvwhY)

        :return original url and generated short url :STATUS 201
        """

        serializer = UrlRandomShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url: str = serializer.data.get('original_url')
            short_url: str = url_shortening(original_url)
            current_site = get_current_site(request)
            data = {
                "original_url": original_url,
                "generated_short_link": f"http://{current_site}/{short_url}",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PremiumClientShortenedUrlView(APIView):
    """ Endpoint that is for users who has premium client status """

    permission_classes = [IsAuthenticated, IsPremiumClient]

    def get(self, request, *args, **kwargs) -> 'Response':  # noqa
        """
        :return -> {"is_premium_client": true}
                    if request.user is premium client
                    OTHERWISE -> {"detail": "You do not have permission to perform this action."}
        """

        return Response({'is_premium_client': request.user.is_premium_client})

    def post(self, request, *args, **kwargs) -> 'Response':  # noqa
        """
        :Requesting original url (for example https://github.com/Kordzakhiaa)
        :Requesting string that is given by premium client
        :Generating short url (for example http://127.0.0.1:8000/{given string by premium client})

        :return original url and generated short url :STATUS 201
        """

        serializer = UrlPremiumClientShortenerSerializer(data=request.data)
        if serializer.is_valid():
            original_url: str = serializer.data.get('original_url')
            given_string: str = serializer.data.get('given_string')

            short_url: str = url_shortening(original_url, given_string)
            current_site = get_current_site(request)
            data = {
                "original_url": original_url,
                "generated_short_link": f"http://{current_site}/{short_url}",
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class RedirectUrlView(APIView):
    """ APIView that provides url redirection """

    def get(self, request, shortened_part: str) -> 'HttpResponseRedirect':  # noqa
        """
        Get method that redirects generated short url to original url

        :type shortened_part: str
        :return HttpResponseRedirect :status 302 (REDIRECT)
        """
        try:
            shortener = UrlShortener.objects.get(short_url=shortened_part)
            shortener.counter += 1  # INCREASING COUNTER
            shortener.save()
            return HttpResponseRedirect(shortener.original_url)  # STATUS HTTP_302_FOUND (REDIRECT)
        except:
            raise Http404('This link is broken!')
