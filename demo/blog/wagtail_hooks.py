from django.http import HttpResponse
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import BlogInnerPage

# http://docs.wagtail.io/en/v2.2/reference/contrib/modeladmin/
class BlogInnerPageAdmin(ModelAdmin):
    model = BlogInnerPage
    menu_label = _('Page')
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    inspect_view_enabled = True  # добавляет дополнительное возможность просмотра статьи
    exclude_from_explorer = False
    list_display = ('title', 'date')
    list_filter = ('title', 'date')
    search_fields = ('title',)


# http://docs.wagtail.io/en/stable/reference/hooks.html
@hooks.register('register_page_listing_buttons')
def page_custom_listing_buttons(page, page_perms, is_parent=False):
    yield wagtailadmin_widgets.ButtonWithDropdownFromHook(
        _('More actions'),
        hook_name='my_button_dropdown_hook',
        page=page,
        page_perms=page_perms,
        is_parent=is_parent,
        priority=50
    )


# http://docs.wagtail.io/en/stable/reference/hooks.html
@hooks.register('my_button_dropdown_hook')
def page_custom_listing_more_buttons(page, page_perms, is_parent=False):
    if page_perms.can_move():
        yield wagtailadmin_widgets.Button('Move', reverse('wagtailadmin_pages:move', args=[page.id]), priority=10)
    if page_perms.can_delete():
        yield wagtailadmin_widgets.Button('Delete', reverse('wagtailadmin_pages:delete', args=[page.id]), priority=30)
    if page_perms.can_unpublish():
        yield wagtailadmin_widgets.Button('Unpublish', reverse('wagtailadmin_pages:unpublish', args=[page.id]),
                                          priority=40)


# http://docs.wagtail.io/en/stable/reference/hooks.html
@hooks.register('before_serve_page')
def block_googlebot(page, request, serve_args, serve_kwargs):
    if request.META.get('HTTP_USER_AGENT') == 'GoogleBot':
        return HttpResponse("<h1>bad googlebot no cookie</h1>")


from wagtail.core import hooks


# http://docs.wagtail.io/en/stable/reference/hooks.html
# проверяю под каким пользователем нахожусь и в зависимосте от того достаю определенные посты
@hooks.register('construct_explorer_page_queryset')
def show_my_profile_only(parent_page, pages, request):
    # If we're in the 'user-profiles' section, only show the user's own profile
    if parent_page.slug == 'blog':
        pages = pages.filter(owner=request.user)

    return pages


from wagtail.admin import widgets as wagtailadmin_widgets


# http://docs.wagtail.io/en/stable/reference/hooks.html
# можно добавить кнопку
@hooks.register('register_page_listing_buttons')
def page_listing_buttons(page, page_perms, is_parent=False):
    yield wagtailadmin_widgets.PageListingButton(
        _('A page listing button'),
        '/goes/to/a/url/',
        priority=10
    )


# http://docs.wagtail.io/en/stable/reference/hooks.html
# можно добавить кнопку в выподающее меню 'больше'
@hooks.register('register_page_listing_more_buttons')
def page_listing_more_buttons(page, page_perms, is_parent=False):
    yield wagtailadmin_widgets.Button(
        _('A dropdown button'),
        '/goes/to/a/url/',
        priority=60
    )


modeladmin_register(BlogInnerPageAdmin)
