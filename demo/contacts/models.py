from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractForm


class FormField(AbstractFormField):
    page = ParentalKey('ContactsPage', on_delete=models.CASCADE, related_name='form_fields')


class ContactsPage(AbstractForm):
    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
    ]

    subpage_types = []

    max_count = 1

    class Meta:
        verbose_name = _('Contact Us')

# Create your models here.
