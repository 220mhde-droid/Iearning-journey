import random
import string

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return f"🛡️ كلمة المرور المقترحة هي: {password}"

print(generate_secure_password(16))