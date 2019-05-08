from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Orderable, Page

from modelcluster.fields import ParentalKey


class Author(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    age = models.IntegerField(verbose_name=_('Age'))

    panels = [
        FieldPanel('name'),
        FieldPanel('age'),
    ]

    class Meta:
        abstract = True


# The real model which combines the abstract model, an
# Orderable helper class, and what amounts to a ForeignKey link
# to the model we want to add related links to (BookPage)
class BookPageRelatedLinks(Orderable, Author):
    page = ParentalKey('books.BookPage', on_delete=models.CASCADE, related_name='related_links')


class BookPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('related_links', label="Related Links"),
    ]

# Create your models here.
