from models import Language, Translation


def get_translation(key: str, language: Language) -> str:
    if translation := Translation.query.filter_by(key=key, language=language).first() is not None:
        return translation.value

    # If the translation is not found, return the key
    return key
