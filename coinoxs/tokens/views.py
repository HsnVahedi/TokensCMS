from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from .models import ERC20DefaultToken, ERC721DefaultToken, TRC20DefaultToken, EthereumNetwork, TronNetwork


class ERC20TokenView(APIView):
    def get(self, request, network, symbol):
        try:
            network = EthereumNetwork.objects.get(name=network)
            token = network.erc20_tokens.get(symbol=symbol)
        except ObjectDoesNotExist:
            token = ERC20DefaultToken.objects.first()
        return HttpResponseRedirect(token.image.file.url)


class ERC721TokenView(APIView):
    def get(self, request, network, symbol):
        try:
            network = EthereumNetwork.objects.get(name=network)
            token = network.erc721_tokens.get(symbol=symbol)
        except ObjectDoesNotExist:
            token = ERC721DefaultToken.objects.first()
        return HttpResponseRedirect(token.image.file.url)


class TRC20TokenView(APIView):
    def get(self, request, network, symbol):
        try:
            network = TronNetwork.objects.get(name=network)
            token = network.trc20_tokens.get(symbol=symbol)
        except ObjectDoesNotExist:
            token = TRC20DefaultToken.objects.first()
        return HttpResponseRedirect(token.image.file.url)
