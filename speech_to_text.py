import subprocess
import re

# TODO
language = "auto"  # "en", "zh", "auto"...
WHISPER_STREAM_PATH = "...your_path.../whisper.cpp/stream"
WHISPER_MODEL_PATH = "...your_path.../whisper.cpp/models/ggml-base.bin"
WHISPER_LOG_FILE_PATH = "...any_path_and_filename..."


def start_whisper():
    global process
    process = subprocess.Popen([WHISPER_STREAM_PATH, "-m", WHISPER_MODEL_PATH, "-l", language, "-t", "8", "--step", "500", "--length", "5000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def process_escape_codes(raw_output):
    # whisper.cpp uses '\33[2K\r' to modify output
    output = raw_output.decode().strip()
    length = len(output)
    for i in range(length-1, 0, -1):
        if output[i] == '\r':
            output = output[i+1:]
            break
    return output

def get_output():
    raw_output = process.stdout.readline()
    if raw_output == b'' and process.poll() is not None:
        return None
    if raw_output:
        return process_escape_codes(raw_output)
    return None

def get_error():
    log_file = open(WHISPER_LOG_FILE_PATH, "w")
    stderr_output = process.stderr.read().decode().strip()
    log_file.write(stderr_output)
    log_file.close()
