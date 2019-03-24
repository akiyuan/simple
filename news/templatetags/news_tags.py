from ..models import Articles
from django import template

register = template.Library()


@register.simple_tag
def total_posts():
    return Articles.objects.count()
