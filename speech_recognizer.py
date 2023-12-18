import io
import speech_recognition as sr
from pydub import AudioSegment

class AudioTranscriberSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioTranscriberSingleton, cls).__new__(cls)
            cls._instance._recognizer = sr.Recognizer()  # Create recognizer instance
            # Add any other initialization code here
        return cls._instance

    def transcribe_audio(self, audio_file_path):
        # Convert OGG to WAV using pydub
        audio = AudioSegment.from_file(audio_file_path, format="ogg")

        # Create a BytesIO object to hold the converted audio data
        buffer = io.BytesIO()

        # Export the converted audio data to the BytesIO object
        audio.export(buffer, format="wav")

        # Load the converted audio data from the BytesIO object
        with sr.AudioFile(buffer) as audio_file:
            # Adjust for ambient noise
            self._recognizer.adjust_for_ambient_noise(audio_file)

            # Listen to the audio and transcribe
            try:
                print("Transcribing audio...")
                audio_data = self._recognizer.record(audio_file)
                text = self._recognizer.recognize_google(audio_data, language="es-ES")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))


# Example usage:
audio_transcriber = AudioTranscriberSingleton()
print(audio_transcriber.transcribe_audio('voice_messages/prueba.ogg'))
