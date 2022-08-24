import os
import shutil
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence

audio_transcript_file = os.listdir("./input")[0]
result_text_file = "./output/result-3.txt"
folder_name = "audio-chunks"

#os.system("ffmpeg -i {} input.wav".format(audio_transcript_file))
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_file(file = path, format = "wav")

    #increase volume by 20db
    soundLouder = sound + 20

    print("Reading and chunking sound: {}".format(soundLouder))
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(soundLouder,
        min_silence_len = 1000,
        silence_thresh = soundLouder.dBFS-26,
        keep_silence=100,
    )
    
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        print("export audio chunk")
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        print("recognizing the chunk")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="fr-FR")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.lower()} \n"
                print(chunk_filename, ":", text)
                whole_text += text
                
    return whole_text
        
text = get_large_audio_transcription("./input/"+audio_transcript_file)
file = open(result_text_file, "w")
file.write(text)
file.close()
shutil.rmtree(folder_name)