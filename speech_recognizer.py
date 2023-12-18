import io
import speech_recognition as sr
from pydub import AudioSegment

class AudioTranscriberSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AudioTranscriberSingleton, cls).__new__(cls)
            cls._instance._recognizer = sr.Recognizer()  # Create recognizer instance
        return cls._instance

    def transcribe_audio(self, audio_file_path):
        audio = AudioSegment.from_file(audio_file_path, format="ogg")

        buffer = io.BytesIO()

        audio.export(buffer, format="wav")

        with sr.AudioFile(buffer) as audio_file:
            self._recognizer.adjust_for_ambient_noise(audio_file)

            try:
                print("Transcribing audio...")
                audio_data = self._recognizer.record(audio_file)
                text = self._recognizer.recognize_google(audio_data, language="es-ES")
                return text
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))



