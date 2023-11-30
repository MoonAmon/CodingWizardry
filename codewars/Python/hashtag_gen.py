def generate_hashtag(s):
    if not s:
        return False
    s = s.lower()
    s = s.title()
    s = ''.join(s.split())
    if len(s) > 140:
        return False
    return '#' + s