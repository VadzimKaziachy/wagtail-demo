from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class City(ClusterableModel):
    city = models.TextField(verbose_name=_('City'))

    panels = [
        MultiFieldPanel([
            FieldPanel('city'),
        ])
    ]

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = _('City')


class CityRelationship(Orderable, models.Model):
    events = ParentalKey('EventsPage',
                         related_name='city_relationship',
                         on_delete=models.CASCADE)
    city = models.ForeignKey('events.City',
                             related_name='city_model',
                             on_delete=models.CASCADE,
                             verbose_name=_('City'))
    panel = [
        SnippetChooserPanel('city')
    ]


@register_snippet
class Country(models.Model):
    """
    Source: https://wagtail-autocomplete.readthedocs.io/en/latest/using_other_models.html
    """

    country = models.TextField(verbose_name=_('Country'))

    panels = [
        MultiFieldPanel([
            FieldPanel('country'),
        ])
    ]

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = _('Country')


class EventsPage(Page):
    country = models.ForeignKey(
        Country,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    content_panels = [
        MultiFieldPanel(Page.content_panels, heading=_('Page title')),
        InlinePanel('city_relationship',
                    panels=None,
                    label=_('city'),
                    min_num=1,
                    max_num=3),
        SnippetChooserPanel('country'),
    ]
