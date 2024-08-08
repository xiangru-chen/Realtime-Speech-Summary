# Realtime-Speech-Summary
Realtime speech summary using Google Gemini, OpenAI Whisper, and Streamlit.

## Installation
### Whisper.cpp
- download [whisper.cpp](https://github.com/ggerganov/whisper.cpp)
  ```bash
  git clone https://github.com/ggerganov/whisper.cpp.git
  ```

- choose [model](https://github.com/openai/whisper/blob/main/README.md#available-models-and-languages) (models are multilingual unless the model name includes `.en`)
  ```bash
  cd whisper.cpp
  bash ./models/download-ggml-model.sh base
  make
  ./main --help
  ```

- [Real-time speech to text](https://github.com/ggerganov/whisper.cpp/tree/master/examples/stream) (install SDL2 first)
  ```bash
  make stream
  ./stream --help
  ```

### Gemini
- Install [Gemini](https://ai.google.dev/gemini-api/docs/quickstart?lang=python) API SDK
  ```bash
  pip install -q -U google-generativeai
  ```
- Get an API key

### Streamlit
Install [Streamlit](https://streamlit.io/)
```bash
pip install streamlit
streamlit hello
```

## Usage
- Enter your API key in [`summary.py`](summary.py)
- Enter the path of whisper.cpp in [`speech_to_text.py`](speech_to_text.py)
- run [`main.py`](main.py) with Streamlit
  ```bash
  streamlit run main.py
  ```

## Info
This is a group project of Microsoft Engage 2024.
