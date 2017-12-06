from django import template
from django.conf import settings
import os

register = template.Library()


@register.simple_tag
def include_ajax_csrf_token():
    url = getattr(settings, 'STATIC_URL') if hasattr(settings, 'STATIC_URL') else getattr(settings, 'MEDIA_URL')
    return "<script type='text/javascript' src='%s'></script>" % os.path.join(url, 'ajax', 'csrf_token.min.js')
