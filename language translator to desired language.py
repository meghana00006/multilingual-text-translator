from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    try:
        # Automatically detect the source language and translate to the target language
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None

if __name__ == '__main__':
    while True:
        # Prompt the user to enter text to translate
        text_to_translate = input("Enter text to translate (enter 'quit' to exit): ")
        
        # Check if the user wants to quit
        if text_to_translate.lower() == 'quit':
            print("Exiting...")
            break
        
        # Prompt the user to enter the full target language name (e.g., 'French', 'Spanish')
        target_language_name = input("Enter the full language name to translate to (e.g., 'French'): ")
        
        # Check if the user wants to quit
        if target_language_name.lower() == 'quit':
            print("Exiting...")
            break
        
        # Translate the text
        translated_text = translate_text(text_to_translate, target_language_name)
        
        if translated_text:
            # Print the translated text
            print(f"Translated text: {translated_text}\n")
