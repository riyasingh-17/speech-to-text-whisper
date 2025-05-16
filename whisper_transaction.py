import whisper

# Whisper model load karo
model = whisper.load_model("base")  # ya "small", "medium", "large"

# Audio file ka path yahan do
result = model.transcribe("deadline.mp3")

# Output print karo
print("Transcription:")
print(result["text"])
