#For testing the voice (BY DEFAULT , it's male)

from __future__ import print_function
import pyttsx


engine = pyttsx.init()
engine.say('This is a hello world program activated by voice. I hope you can hear me..')
print("This is a hello world program activated by voice. I hope you can hear me..")

engine.runAndWait()



#For checking voices available
"""import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   print (voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()"""

#For keeping female voice
"""import pyttsx
engine = pyttsx.init()
x='This is a hello world program with voice . I hope you can hear me...'
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.say(x)
print(x)
engine.runAndWait()"""



