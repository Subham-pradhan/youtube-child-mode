import re

BAD_KEYWORDS = [
    "sex", "drugs", "violence", "kill", "hate", "naked", "murder", "blood",
    "suicide", "alcohol", "abuse", "fight", "porn", "racist", "shoot", "weapon"
]

BAD_PATTERN = re.compile(r'\b(' + '|'.join(BAD_KEYWORDS) + r')\b', re.IGNORECASE)

def is_child_safe(text):
    if not text.strip():
        return True
    return not bool(BAD_PATTERN.search(text))
