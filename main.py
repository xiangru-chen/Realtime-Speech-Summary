import summary
import speech_to_text

import streamlit as st


# Streamlit UI
col1, col2 = st.columns(2)
with col1:
    st.header("speech-to-text output")
with col2:
    st.header("summary")


summary.setup_api()
speech_to_text.start_whisper()  


while True:
    output = speech_to_text.get_output()
    if output is None:
        break
    print(output, flush=True)
    col1.markdown(output)
    response = summary.get_response(output)
    col2.markdown(response)

speech_to_text.get_error()
