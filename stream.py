import streamlit as st
import speech_recognition as sr
import requests

# Initialize the speech recognizer
r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        st.write("Recording...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        st.write("Recording stopped.")
        return audio

def recognize_audio(audio):
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return "Could not request results from the speech recognition service; {0}".format(e)

def send_to_api(text):
    url = 'https://f6e6-35-230-58-190.ngrok-free.app/generate'  # Replace with your actual ngrok URL
    response = requests.post(url, json={'Query': text})
    return response.json()

def main():
    st.title("Speech to Code Application")

    if st.button("Record Speech"):
        audio = record_audio()
        text = recognize_audio(audio)
        st.text_area("Recognized Text", value=text, height=150)

        if text not in ["Speech Recognition could not understand the audio", 
                        "Could not request results from the speech recognition service"]:
            response = send_to_api(text)
            st.text("API Response:")
            st.json(response)

            # Assuming the API returns a text response that needs to be split and displayed
            if 'response' in response:
                parts = response['response'].split("<</SYS>>")
                desired_text = "<</SYS>>".join(parts[2:5])
                st.text_area("Extracted Text", value=desired_text, height=150)

if __name__ == "__main__":
    main()
