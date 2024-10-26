import hashlib

def coder_password(text):
    return hashlib.sha256(text.encode()).hexdigest()