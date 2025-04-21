BAD_KEYWORDS = [
    "sex", "drugs", "violence", "kill", "hate", "naked", "murder", "blood",
    "suicide", "alcohol", "abuse", "fight", "porn", "racist", "shoot", "weapon"
]

def is_child_safe(text):
    if not text.strip():
        return True
    lower_text = text.lower()
    for word in BAD_KEYWORDS:
        if word in lower_text:
            return False
    return True
