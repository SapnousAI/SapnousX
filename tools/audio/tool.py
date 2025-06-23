try:
    import pyttsx3
    import whisper
    audio_available = True
except ImportError:
    audio_available = False

def text_to_speech(text, filename='output.wav'):
    if not audio_available:
        return 'pyttsx3 not installed.'
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return f'TTS saved to {filename}'

def speech_to_text(audio_path):
    if not audio_available:
        return 'whisper not installed.'
    model = whisper.load_model('base')
    result = model.transcribe(audio_path)
    return result['text']
