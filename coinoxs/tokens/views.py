from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from .models import ERC20Token, ERC20DefaultToken, ERC721Token, ERC721DefaultToken


class ERC20TokenView(APIView):
    def get(self, request, symbol):
        try:
            token = ERC20Token.objects.get(symbol=symbol)
        except ObjectDoesNotExist:
            token = ERC20DefaultToken.objects.first()
        return HttpResponseRedirect(token.image.file.url)


class ERC721TokenView(APIView):
    def get(self, request, symbol):
        try:
            token = ERC721Token.objects.get(symbol=symbol)
        except ObjectDoesNotExist:
            token = ERC721DefaultToken.objects.first()
        return HttpResponseRedirect(token.image.file.url)
