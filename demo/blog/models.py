from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel


class BlogInnerPage(Page):
    email = models.EmailField(verbose_name='Email',
                              max_length=255,
                              null=True,
                              blank=False)

    date = models.DateField(verbose_name=_('Date'),
                            null=True)
    is_important = models.BooleanField(verbose_name=_('Active'),
                                       default=True)
    content_panels = [
        MultiFieldPanel(Page.content_panels, heading=_('Page title')),
        MultiFieldPanel([
            FieldPanel('email'),
            FieldPanel('is_important'),
            FieldPanel('date'),
        ], heading=_('Description'))
    ]

    # Specifies what content types can exist as children of BlogInnerPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

    # Specifies parent to BlogInnerPage as being BlogPage
    parent_page_types = ['BlogPage']

    class Meta:
        verbose_name = _('Blog inner page')
        verbose_name_plural =_('Blog inner pages')


class BlogPage(Page):
    content_panels = [MultiFieldPanel(Page.content_panels, heading=_('Page title'))]

    max_count = 1

    subpage_types = ['BlogInnerPage']

    class Meta:
        verbose_name = _('Blog page')

# Create your models here.
