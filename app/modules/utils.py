import re

def validate_youtube_url(url: str) -> bool:
    regex = r"(https?://)?(www\.)?(youtube|youtu)\.(com|be)/.+"
    return re.match(regex, url) is not None
