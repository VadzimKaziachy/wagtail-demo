from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey


class City(ClusterableModel):
    city = models.TextField(verbose_name=_('City'))

    panels = [
        MultiFieldPanel([
            FieldPanel('city'),
        ])
    ]

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


class EventsPage(Page):
    content_panels = [
        MultiFieldPanel(Page.content_panels, heading=_('Page title')),
        InlinePanel('city_relationship',
                    panels=None,
                    label=_('city'),
                    min_num=1,
                    max_num=3)
    ]
