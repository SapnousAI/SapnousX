try:
    import ffmpeg
    video_available = True
except ImportError:
    video_available = False

def extract_audio(video_path, audio_path='output_audio.wav'):
    if not video_available:
        return 'ffmpeg-python not installed.'
    (
        ffmpeg
        .input(video_path)
        .output(audio_path)
        .run(overwrite_output=True)
    )
    return f'Audio extracted to {audio_path}'
