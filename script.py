def process_data(text, target_language):
    from googletrans import Translator
    translator=Translator()
    translated_text=translator.translate(text,dest=target_language)
    translated_msg= f"{translated_text.text}"
    return translated_msg
