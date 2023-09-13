from gtts import gTTS

tts = gTTS('Иван Федорович Крузенштерн. Человек и пароход!', lang='ru')
tts.save('tts_output.mp3')