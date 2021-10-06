from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel


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
    def __str__(self):
        return f'ERC20 - {self.symbol}'

    class Meta:
        verbose_name = "ERC20 Token"
        verbose_name_plural = "ERC20 Tokens"


@register_snippet
class ERC721Token(Token):
    def __str__(self):
        return f'ERC721 - {self.symbol}'

    class Meta:
        verbose_name = "ERC721 Token"
        verbose_name_plural = "ERC721 Tokens"


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
