# Speech-to-Text using OpenAI Whisper

This project is a Python-based speech-to-text converter using OpenAI's Whisper model. It takes an audio file as input and outputs the transcribed text.

## Features

- Converts speech (in .mp3 or .wav) to text
- Uses OpenAI Whisper model (base version)
- Simple and easy to use

## How it Works

1. The Python script loads the Whisper model.
2. It reads the audio file provided.
3. It transcribes the speech content into text.
4. The transcribed text is printed as output.

## Requirements

Install the following packages before running:

```bash
pip install openai-whisper
pip install torch
