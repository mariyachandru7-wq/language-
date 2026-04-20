from deep_translator import GoogleTranslator

text = input("Enter text: ")
translated = GoogleTranslator(source='auto', target='ta').translate(text)

print("Translated:", translated)