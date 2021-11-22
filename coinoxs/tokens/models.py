from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


class Network(models.Model):
    name = models.TextField(primary_key=True)
    panels = [
        FieldPanel('name'),
    ]

    class Meta:
        abstract = True


@register_snippet
class EthereumNetwork(Network):
    def __str__(self):
        return f'Ethereum - {self.name}'

    class Meta:
        verbose_name = "Ethereum Network"
        verbose_name_plural = "Ethereum Networks"


@register_snippet
class TronNetwork(Network):
    def __str__(self):
        return f'Tron - {self.name}'

    class Meta:
        verbose_name = "Tron Network"
        verbose_name_plural = "Tron Networks"


class Token(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    symbol = models.TextField(primary_key=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('symbol'),
    ]

    class Meta:
        abstract = True


@register_snippet
class ERC20Token(Token):
    network = models.ForeignKey(
        to=EthereumNetwork,
        on_delete=models.SET_NULL,
        related_name='erc20_tokens',
        default=None,
        null=True,
        blank=True,
    )

    panels = Token.panels + [
        SnippetChooserPanel('network')
    ]

    def __str__(self):
        return f'ERC20 - {self.symbol}'

    class Meta:
        verbose_name = "ERC20 Token"
        verbose_name_plural = "ERC20 Tokens"


@register_snippet
class ERC721Token(Token):
    network = models.ForeignKey(
        to=EthereumNetwork,
        on_delete=models.SET_NULL,
        related_name='erc721_tokens',
        default=None,
        null=True,
        blank=True,
    )

    panels = Token.panels + [
        SnippetChooserPanel('network')
    ]

    def __str__(self):
        return f'ERC721 - {self.symbol}'

    class Meta:
        verbose_name = "ERC721 Token"
        verbose_name_plural = "ERC721 Tokens"


@register_snippet
class TRC20Token(Token):
    network = models.ForeignKey(
        to=TronNetwork,
        on_delete=models.SET_NULL,
        related_name='trc20_tokens',
        default=None,
        null=True,
        blank=True,
    )

    panels = Token.panels + [
        SnippetChooserPanel('network')
    ]

    def __str__(self):
        return f'TRC20 - {self.symbol}'

    class Meta:
        verbose_name = "TRC20 Token"
        verbose_name_plural = "TRC20 Tokens"


class DefaultToken(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]

    class Meta:
        abstract = True


@register_snippet
class ERC20DefaultToken(DefaultToken):
    class Meta:
        verbose_name_plural = "ERC20 Default Tokens"
        verbose_name = "ERC20 Default Token"


@register_snippet
class ERC721DefaultToken(DefaultToken):
    class Meta:
        verbose_name_plural = "ERC721 Default Tokens"
        verbose_name = "ERC721 Default Token"


@register_snippet
class TRC20DefaultToken(DefaultToken):
    class Meta:
        verbose_name_plural = "TRC20 Default Tokens"
        verbose_name = "TRC20 Default Token"
