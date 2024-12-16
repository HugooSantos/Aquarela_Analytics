from bcrypt import hashpw, gensalt, checkpw

def hash_password(password: str) -> str:
    """
    Generates a secure hash for the password using bcrypt.
    """
    hashed = hashpw(password.encode('utf-8'), gensalt())
    return hashed.decode('utf-8')  # Retorna como string para salvar no banco

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Checks if the password matches the stored hash.
    """
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))