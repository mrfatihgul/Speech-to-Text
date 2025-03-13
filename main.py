import speech_recognition as sr

def speech_to_text_and_save():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("|---------------|\n"
              "|Say something: |\n"
              "|---------------|")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("|---------------|\n"
              "|Recognizing... |\n"
              "|---------------|")
        text = recognizer.recognize_google(audio)
        print(f"Text: {text}")

        with open("transcribed_text.txt", "w") as file:
            file.write(text)
            print("|------------------------------------------------|\n"
                  "|Transcribed text saved to transcribed_text.txt  |\n"
                  "|------------------------------------------------|")
    except sr.UnknownValueError:
        print("|----------------------------|\n"
              "|Could not understand audio. |\n"
              "|----------------------------|")
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")

if __name__ == "__main__":
    speech_to_text_and_save()