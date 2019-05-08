from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _

from xml.etree.ElementTree import fromstring

@deconstructible
class ProhibitBlankRichTextValidator:
    """
    Validate that the incoming html-string contains plain text characters.
    """

    message = _('This field is required')

    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __call__(self, value):
        plain_text = ''.join(fromstring('<rich-text>{}</rich-text>'.format(value)).itertext())
        if not plain_text:
            raise ValidationError(self.message)