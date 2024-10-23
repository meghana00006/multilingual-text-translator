from googletrans import Translator, LANGUAGES

def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None

def translate_text(text, dest_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text, translation.src

if __name__ == '__main__':
    while True:
        # Prompt the user to enter text to translate
        text_to_translate = input("Enter text to translate (enter 'quit' to exit): ")
        
        # Check if the user wants to quit
        if text_to_translate.lower() == 'quit':
            print("Exiting...")
            break
        
        # Detect the language of the input text
        translator = Translator()
        detected_lang = translator.detect(text_to_translate).lang
        
        # Print detected language and language code
        print(f"Detected language: {LANGUAGES[detected_lang]} ({detected_lang})")
        
        # Prompt the user to enter the target language name
        target_language_name = input("Enter the full language name to translate to (e.g., 'French'): ")
        
        # Check if the user wants to quit
        if target_language_name.lower() == 'quit':
            print("Exiting...")
            break
        
        # Get the language code for the target language name
        dest_language = get_language_code(target_language_name)
        
        # Validate the destination language
        if not dest_language:
            print(f"Error: Language '{target_language_name}' not recognized. Please try again.")
            continue
        
        # Translate the text
        translated_text, source_lang = translate_text(text_to_translate, dest_language)
        
        # Check if the detected language and target language are the same
        if detected_lang == dest_language:
            print(f"The text is already in {LANGUAGES[dest_language]}.")
        else:
            # Print translated text and source language
            print(f"Translated text ({LANGUAGES[source_lang]} to {LANGUAGES[dest_language]}): {translated_text}\n")