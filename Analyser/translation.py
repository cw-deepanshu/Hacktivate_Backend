from translate import Translator as MyTranslator
from transcription import get_transcript_text



# Create a translator object
translator = MyTranslator(to_lang="en", from_lang="hi")

# with open("transcript.txt", "r", encoding="utf-8") as file:
#     saved_transcript = file.read()

# # Use the saved transcript as needed
# print(saved_transcript)

# # Hindi text to be translated
# hindi_text = 'नमस्ते दुनिया'

# Translate Hindi text to English

def get_translation(lang, filename) :
        transcript_text = get_transcript_text(lang,filename)
        translation = translator.translate(transcript_text)
        return translation

# Print the translated text
# print(translation)
