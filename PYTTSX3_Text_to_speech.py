#Converting text to voice
#To install this library :pip install pyttsx3
#By - Atul Jha

import pyttsx3 as p
engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
volume = engine.getProperty("volume")
engine.setProperty("volume",1.0)
rate = engine.getProperty("rate")
engine.setProperty('rate', 170)
engine.say("Hello sir how's everything going")
engine.say("Kaise ho?")
engine.runAndWait()
