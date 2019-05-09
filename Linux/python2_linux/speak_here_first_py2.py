from __future__ import print_function
import speech_recognition as sr
import os

#obtain audio from the microphone
r = sr.Recognizer()

with sr.Microphone() as source:
	print("Speak into the microphone")
	audio = r.listen(source)
	
rec=r.recognize_google(audio)

print("You said "+rec)

if(rec=='open hello world'):
        print("Opening file...")
        os.system("hello_world.py")
        

#try:
#print("Transcription: " +rec)
#if(rec=="Gimmick"):
#        print("Detected")
"""except sr.UnknownValueError:
	print("Audio unintelligible")
except sr.RequestError as e:
	print("Cannot obtain results; {0}" , format(e))"""
