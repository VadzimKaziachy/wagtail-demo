from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, InlinePanel
from wagtail.core.models import Orderable, Page
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


# ======================================================
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


# ======================================================

# https://docs.djangoproject.com/en/2.2/topics/db/models/#multi-table-inheritance
class Article(models.Model):
    article = models.TextField(verbose_name=_('Article'))
    article_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = _('Article')


class Post(models.Model):
    post = models.TextField(verbose_name=_('Post'))
    book_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = _('Post')


class BookReview(Page, Post, Article):
    content_panels = [
        MultiFieldPanel(Page.content_panels + [
            FieldPanel('article'),
            FieldPanel('post'),
        ], heading=_('Book reviews'))
    ]

    class Meta:
        verbose_name = _('Book review')


# ======================================================

@register_snippet
class Genre(models.Model):
    genre = models.CharField(max_length=255)

    panels = [
        MultiFieldPanel([
            FieldPanel('genre'),
        ])
    ]

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = _('Genre')


# ======================================================
@register_snippet
class PublishingHouse(ClusterableModel):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=200)

    panels = [
        FieldPanel('name'),
        InlinePanel('city', label='Pages')
    ]

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('Publishing house')


class City(Orderable):
    category = ParentalKey(
        'books.PublishingHouse',
        related_name='city'
    )
    city = models.CharField(verbose_name=_('City'),
                            max_length=200,
                            blank=True)
    panels = [
        FieldPanel('city')
    ]

    def __str__(self):
        return self.category.name

    class Meta(Orderable.Meta):
        verbose_name = _('City')
# ======================================================
