import html
from django import template

register = template.Library()

@register.filter
def unescape(value):
    """Convertit les entités HTML (&eacute; → é, etc.) en caractères normaux"""
    return html.unescape(value)
