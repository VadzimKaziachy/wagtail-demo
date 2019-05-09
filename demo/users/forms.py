from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm

# http://docs.wagtail.io/en/v2.1.1/advanced_topics/customisation/custom_user_models.html

class CustomUserEditForm(UserEditForm):
    country = forms.CharField(required=True, label=_("Country"))