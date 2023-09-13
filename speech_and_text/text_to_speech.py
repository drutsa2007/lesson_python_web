import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'ru')
voices = engine.getProperty('voices')

engine.say("Текст на русском языке")
engine.runAndWait()
engine.stop()

# # save to file
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()
