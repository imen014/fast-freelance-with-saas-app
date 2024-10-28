# fallahin_freelance_app/templatetags/form_tags.py
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Ajoute une classe CSS à un champ de formulaire."""
    return field.as_widget(attrs={'class': css_class})
