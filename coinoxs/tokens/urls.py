from django.urls import path
from .views import ERC20TokenView, ERC721TokenView

urlpatterns = [
    path('erc20/<str:symbol>', ERC20TokenView.as_view(), name='erc20-token'),
    path('erc721/<str:symbol>', ERC721TokenView.as_view(), name='erc721-token'),
]