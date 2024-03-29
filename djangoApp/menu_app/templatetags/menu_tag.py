from django import template
from django.template import RequestContext

from ..models import MenuBar

register = template.Library()


@register.inclusion_tag('menu/menu_pattern.html', takes_context=True)
def draw_menu(context=RequestContext, menu_name=''):
    url_path = (context.request.path).replace("/", "")
    menu_queryset = MenuBar.objects.filter(category__name=menu_name).select_related('parent')
    haveChild = have_children(menu_queryset)
    return {'menu': menu_queryset, 'haveChild': haveChild, 'url_path': url_path}


def have_children(query):
    menuListChild = []
    for item in query:
        if item.parent != None:
            menuListChild.append(str(item.parent))
    return list(set(menuListChild))

