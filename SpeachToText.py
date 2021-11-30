# env requirement for 4 steps

# 1.pip install speechrecognition
# 2.pip install pyttsx3
# 3.pip install pipwin
# 4.pipwin install pyaudio

# reference: https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# "MyText" is the output text when turn voice to text
# "command" is the input text when turn text to voice 

# Python program to translate
# speech to text and text to speech
  
import pyttsx3 
import speech_recognition as sr

  
# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
      
# Loop infinitely for user to
# speak
  
# while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
#listen and turn to text once
def SpeechToText():
    try:
            
        # use the microphone as source for input.
        with sr.Microphone() as source2:
                
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=1)
            print("I am listening")
            #listens for the user's input 
            audio2 = r.listen(source2)
            print("listening successfully")
            # Using google to recognize audio
            #MyText = r.recognize_google(audio2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say "+MyText)
            #SpeakText(InputText)
            return MyText
                
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
        print("unknown error occured")
