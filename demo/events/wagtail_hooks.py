from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import City


class CityAdmin(ModelAdmin):
    model = City
    menu_label = _('Cities')
    menu_icon = 'site'
    list_display = ('city', )


class Directiries(ModelAdminGroup):
    menu_label = _('Directiries')
    menu_icon = 'form'
    menu_order = 300
    items = (CityAdmin,)


modeladmin_register(Directiries)
