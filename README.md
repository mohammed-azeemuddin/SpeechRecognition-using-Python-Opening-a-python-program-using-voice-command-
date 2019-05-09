# SpeechRecognition-using-Python (Opening-a-python-program-using-voice-command)
Opens a python program using your custom voice command

### Windows:

  **Python 3.3+ :** 

  **Requirements installation:**

  ```pip install SpeechRecogntion```

  ```pip install pyaudio(For mic)```

  ```pip install pyttsx3(For text to speech)```

  **Testing SpeechRecogntion:**
  
  ```python -m speech_recognition```
  
  **Running the program:**
   
   From the downloaded /cloned repo directory , open and execute  speak_here_first.py
   
   (Image)

   Say "open hello world" in the mic , the script then runs hello_world.py (Image)
   through your voice and you will hear a male-voice speaking something and then the program exits.

   **Making modifications:**

   In speak_here_first.py
   If you want your program to execute then change the line to the name of the program  you
   want it to open . (Make sure it is in the same directory as speak_here_first.py or else
   provide  full path to the filename in your system)

   In hello_world.py
   If you want your program to speak anything else rather than the default output,
   you can change the text in it to any other string of your choice.
   You can choose a different voice by un-commenting the second
   section of the program.
   You can change the voice to female by removing the comments in the 
   third section.


