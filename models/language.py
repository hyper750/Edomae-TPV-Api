import enum

from settings import AVAILABLE_LANGUAGES

Language = enum.Enum('Language', [
    [lang, lang]
    for lang in AVAILABLE_LANGUAGES
])
