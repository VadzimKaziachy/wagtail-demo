from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page, Orderable
from django.utils.translation import ugettext_lazy as _


# ============================================
# https://stackoverflow.com/questions/51327668/wagtail-pagechooserpanel-not-showing-up
class ModelCar(models.Model):
    model = models.CharField(verbose_name=_('Model'), max_length=255)
    type = models.CharField(verbose_name=_('Type'), max_length=255)

    panels = [
        FieldPanel('model'),
        FieldPanel('type'),
    ]

    class Meta:
        abstract = True


class CarPageRelatedLinks(Orderable, ModelCar):
    page = ParentalKey('cars.CarPage', on_delete=models.CASCADE, related_name='related_link_cars')


class CarPage(Page):
    title_car = models.TextField()
    date = models.DateField()

    content_panels = [
        MultiFieldPanel(Page.content_panels, heading=_('Page title')),
        MultiFieldPanel([
            FieldPanel('title_car', classname="full title"),
            FieldPanel('date'),
        ], heading=_('Content'))
    ]
    sidebar_content_panels = [
        InlinePanel('related_link_cars', label=_("Car")),
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading=_('Content')),
        ObjectList(sidebar_content_panels, heading=_('Sidebar content')),
        ObjectList(Page.promote_panels, heading=_('Promote')),
        ObjectList(Page.settings_panels, heading=_('Settings'), classname="settings"),
    ])

    class Meta:
        verbose_name = _('Car')
