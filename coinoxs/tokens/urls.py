from django.urls import path
from .views import ERC20TokenView, ERC721TokenView, TRC20TokenView

urlpatterns = [
    path('<str:network>/erc20/<str:symbol>', ERC20TokenView.as_view(), name='erc20-token'),
    path('<str:network>/erc721/<str:symbol>', ERC721TokenView.as_view(), name='erc721-token'),
    path('<str:network>/trc20/<str:symbol>', TRC20TokenView.as_view(), name='trc20-token'),
]
