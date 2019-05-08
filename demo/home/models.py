from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .validators import ProhibitBlankRichTextValidator


class HomePage(Page):
    short_description = RichTextField(verbose_name=_('Short description'),
                                      null=True,
                                      validators=[ProhibitBlankRichTextValidator()])
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name=_('Background image'),
    )

    #  Meta tags
    meta_key_words = models.TextField(blank=True,
                                      max_length=255,
                                      verbose_name=_('SEO keywords'))

    Page.content_panels[0].classname = 'class-fix-panels'

    content_panels = [MultiFieldPanel(
        Page.content_panels + [
            FieldPanel('short_description'),
            ImageChooserPanel('image'),
        ], heading=_('Home'))]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels + [
            FieldPanel('meta_key_words'),
        ], _('Common page configuration'))
    ]

    # Maximum number of pages created
    max_count = 1

    class Meta:
        verbose_name = _('Home')
