import speech_recognition as sr

# This function translate speech to text
def speech_to_text():
    
    # Allows the microphone listen user
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        # Reduces environment noise
        microphone.adjust_for_ambient_noise(source)
        
        # Ready to listen
        print("Diga alguma coisa: ")
        
        # Store audio on variable
        audio = microphone.listen(source)
        
        try:
            # Call recognizer with audio and language
            text = microphone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + text)
        
        # If recognizer don't understand
        except sr.UnkownValueError:
            print("Não entendi")
        
        return text

speech_to_text()