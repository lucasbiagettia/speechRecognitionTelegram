import transformers

model = transformers.AutoModelForSpeechRecognition.from_pretrained("facebook/wav2vec2-large-xlsr-53-german")

# Cargar el archivo de audio
wav = librosa.load("/home/lucasbiagetti/Documentos/gitPr/speechRecognitionTelegram/voice_messages/pruebawav.wav")

# Convertir el archivo de audio a un tensor
audio_tensor = torch.tensor(wav)

# Desgrabar el archivo de audio
transcript = model(audio_tensor).logits.argmax(dim=-1)

# Convertir la transcripción a texto
transcript = transcript.cpu().numpy().tolist()

# Imprimir la transcripción
print(transcript)
