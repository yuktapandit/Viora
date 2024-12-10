import text_to_speech
import datetime
import webbrowser
import weather

def Action(send):
    user_data = send.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is Viora")
        return "My name is Viora"
        
    elif "hello" in user_data or "hii" in user_data:
        text_to_speech.text_to_speech("Hello, how can I help you?")
        return "Hello, how can I help you?"
        
    elif "good morning" in user_data:
        text_to_speech.text_to_speech("Good Morning")
        return "Good Morning"
        
    elif "What is the time now" in user_data or "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " Hour : " , (str)(current_time.minute) + "Minute"  
        text_to_speech.text_to_speech(Time)
        return str(Time)
        
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Okay!! Nice meeting you. Have a good day")
        return "Okay!! Nice meeting you. Have a good day"
    
    elif "bye" in user_data or "goodbye" in user_data:
        text_to_speech.text_to_speech("Good Bye!!!")
        return "Good Bye!!!"
        
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Spotify is ready now, hope you enjoy it")
        return "Spotify is ready now, hope you enjoy it"
        
    elif "open youtube" in user_data or "play youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Youtube is ready now, hope it's a pleasent time")
        return "Youtube is ready now, hope it's a pleasent time"
        
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Google is ready now for you") 
        return "Google is ready now for you"   

    elif "open gmail" in user_data:
        webbrowser.open("https://www.gmail.com/")
        text_to_speech.text_to_speech("Opening gmail")
        return "Opening gmail"
        
    elif "weather" in user_data:
        ans = weather.weather()
        text_to_speech.text_to_speech(ans)
        return ans
        
    else:
        text_to_speech.text_to_speech("Sorry, I am not able to understand you.")
        return "Sorry, I am not able to understand you."
