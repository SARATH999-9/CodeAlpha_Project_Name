import streamlit as st
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice commands
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return "None"
        return command.lower()

# Function to process commands
def process_command(command):
    if 'play' in command:
        song = command.replace('play', '').strip()
        speak(f'Playing {song}')
        pywhatkit.playonyt(song)
    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        if person:  # Ensure the query is not empty
            try:
                info = wikipedia.summary(person, sentences=2)
                speak(info)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Multiple results found for {person}. Please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak(f"Sorry, I couldn't find any information about {person}.")
            except wikipedia.exceptions.WikipediaException as e:
                speak("Sorry, there was an error fetching data from Wikipedia.")
        else:
            speak("Please specify a name or topic.")
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop
if __name__ == "__main__":
    speak("Hello, I am your custom voice assistant. How can I help you today?")
    while True:
        command = take_command()
        if command != "None":
            process_command(command)