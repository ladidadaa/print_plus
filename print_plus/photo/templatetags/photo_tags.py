from django import template
from photo.models import *

register = template.Library()

@register.filter
def subtract(value, arg):
    length = len(value) - len(arg)
    lists = []
    for i in range(length):
        lists.append(i)
    return lists