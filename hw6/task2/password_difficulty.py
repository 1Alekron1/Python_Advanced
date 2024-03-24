import re

with open('/usr/share/dict/words', 'r') as f:
    english_words = set(word.strip().lower() for word in f if len(word.strip()) > 4)


def is_strong_password(password):
    words = re.findall(r'\w{5,}', password.lower())

    for word in words:
        if word in english_words:
            return False
    return True


password = "MyP@ssw0rd"
if is_strong_password(password):
    print("Пароль является хорошим по новым стандартам безопасности")
else:
    print("Пароль не является хорошим по новым стандартам безопасности")
