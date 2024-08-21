import hashlib

def coder(text):
    return hashlib.sha256(text.encode()).hexdigest()