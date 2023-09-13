import speech_recognition as sr

r = sr.Recognizer()
# print('\n'.join(sr.Microphone.list_microphone_names()))  # выбрать нужный
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, name)
# и вставить сюда device_index=2
mic = sr.Microphone(device_index=2)

with mic as audio_file:
    print("Говорите")
    r.adjust_for_ambient_noise(audio_file, duration=0.5)
    audio = r.listen(audio_file)
    print("Идет обработка...")
    try:
        print("Вы сказали: " + r.recognize_google(audio, language='ru-RU', show_all=True))
    except Exception as e:
        print("Ошибка: " + str(e))
