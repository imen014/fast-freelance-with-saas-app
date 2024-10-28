import re

def extract_youtube_id(url):
    match = re.match(r'.*?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^&\n]{11})', url)
    if match:
        return match.group(1)
    return None



def is_youtube_video(url):
    youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    return re.match(youtube_regex, url) is not None


# Fonction pour vérifier si l'URL est potentiellement inappropriée
def is_inappropriate_content(url):
    inappropriate_keywords = ['porn', 'sex', 'adult', 'xxx']  # Liste de mots clés
    return any(keyword in url.lower() for keyword in inappropriate_keywords)