from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def replace_words_with_links(text, replacements):
    for word, url in replacements.items():
        # Создаем список вариантов с окончаниями
        variations = [
            word, word + "а", word + "е", word + "у", word + "ом", word + "ой", word + 'ы',
                  word[:-1] + "а", word[:-1] + "е", word[:-1] + "у", word[:-1] + "ы", word[:-1] + "ой", word[:-1] + "и", word[:-1] + "я", word[:-1]
        ]

        # Создаем паттерн для поиска всех вариантов
        pattern = re.compile(rf'\b({"|".join(map(re.escape, variations))})\b', flags=re.IGNORECASE)

        # Используем sub для замены, но выводим исходное слово
        def replacement(match):
            return f'<a href="{url}" class="card-title text-decoration-none">{match.group(0)}</a>'

        text = pattern.sub(replacement, text)

    return mark_safe(text)




