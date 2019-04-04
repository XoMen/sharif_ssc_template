from django import template
from app_sharif.models import slider

register = template.Library()

@register.filter
def slides(myslide):
    html='   '
    return html
