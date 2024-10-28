import re
from django import template

register = template.Library()

@register.filter
def is_youtube_video(url):
    youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    return re.match(youtube_regex, url) is not None

@register.filter
def is_inappropriate_content(url):
    inappropriate_keywords = ['porn', 'sex', 'adult', 'xxx']  # Liste de mots clés
    return any(keyword in url.lower() for keyword in inappropriate_keywords)
