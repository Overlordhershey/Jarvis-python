#import library

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable


class Listen:

    def __init__(self):
        self.audio_text = ""

    def listen(self):
       with sr.Microphone() as source:
        print("Talk")
        self.audio = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            self.audio_text = r.recognize_google(self.audio)
            # using google speech recognition
            print("You: "+self.audio_text)
        except:
            print("Sir, I did not get that") 


        

listener = Listen()

listener.listen()


