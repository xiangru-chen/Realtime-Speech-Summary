import summary
import speech_to_text

import streamlit as st
import time

# Streamlit UI
col1, col2 = st.columns(2)
with col1:
    st.header("speech-to-text output")
with col2:
    st.header("summary")


summary.setup_api()
speech_to_text.start_whisper()  


while True:
    # print out the spending time
    start_time_output = time.time()
    output = speech_to_text.get_output()
    end_time_output = time.time()
    print(f"speech_to_text spent {end_time_output - start_time_output} seconds")
    
    if output is None:
        break
    print(output, flush=True)
    col1.markdown(output)
    # print out the spending time
    start_time_output = time.time()
    response = summary.get_response(output)
    end_time_output = time.time()
    print(f"summary spent {end_time_output - start_time_output} seconds")
    col2.markdown(response)

speech_to_text.get_error()
