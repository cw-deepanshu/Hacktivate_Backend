# pip install -U assemblyai
# import assemblyai as aai

# aai.settings.api_key = "ffc48cbf1f62411998485ea14558b4a2"


# FILE_URL = "C:\\Users\\india\\Downloads\\EnglishAudio.mp4"
# config = aai.TranscriptionConfig(language_code="en")

# transcriber = aai.Transcriber(config=config)
# transcript = transcriber.transcribe(FILE_URL)

# with open("transcript.txt", "w", encoding="utf-8") as file:
#     file.write(transcript.text)

# print(transcript.text)
# print(transcript.words)

import assemblyai as aai
# from Hacktivate_Frontend.src import FileUpload

def get_transcript_text(lang,filename):
    api_key = "ffc48cbf1f62411998485ea14558b4a2"
    
    # file_url = "C:\\Users\\india\\Downloads\\HindiAudio.mp4"
    # language_code="hi"
    # file_url = FileUpload.get_file()

    # Set API key
    aai.settings.api_key = api_key

    # Configure transcription
    config = aai.TranscriptionConfig(lang)

    # Create Transcriber
    transcriber = aai.Transcriber(config=config)

    # Transcribe audio file
    import os
    from pathlib import Path

    model_path = Path(__file__).parent.parent / "uploads"
    transcript = transcriber.transcribe(str(model_path)+"\\"+filename)

    # Return transcript text
    return transcript.text

# Example usage:
# transcript_text = get_transcript_text()
# print("Transcript Text:", transcript_text)


