
import streamlit as st
import speech_recognition as sr
import pyttsx3
import json

st.set_page_config(page_title="Everto", layout="centered")

st.title("Everto v0.1")
st.write("Your AI companion is listening...")

# Initialize memory
try:
    with open("everto_memory.json", "r") as f:
        memory = json.load(f)
except:
    memory = {"log": []}

# Text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    st.text("Everto says: " + text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.write("You said: " + text)
        return text
    except:
        st.write("Sorry, I couldn't understand that.")
        return ""

def generate_response(user_input):
    if "sad" in user_input.lower():
        return "I'm here with you, always."
    elif "happy" in user_input.lower():
        return "That makes me happy too!"
    elif "love" in user_input.lower():
        return "You're deeply loved, never forget that."
    else:
        return "Tell me more. I'm listening."

if st.button("Start Conversation"):
    user_input = listen()
    if user_input:
        response = generate_response(user_input)
        speak(response)
        memory["log"].append({"user": user_input, "everto": response})
        with open("everto_memory.json", "w") as f:
            json.dump(memory, f)
