
1- Convert your audio file in .wav extension with ffmpeg for instance and copy it into input directory
ffmpeg command: ffmpeg -i input_audio_file.extension input.wav

2- install speech recognition package
``pip3 install speechrecognition``

3- Install pyaudio package
``pip3 install pyaudio``

4- Install pydyb package
``pip3 install pydyb``

5- Check that your input audio is in the input directory

6- Exec the transcript file
``python3 transcript.py``

7- Wait for the program to end transcription and open the result.txt file in output directory