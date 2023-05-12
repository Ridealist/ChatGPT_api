from gtts import gTTS
from playsound import playsound

# input
text = """
I strongly believe that college entrance examinations should solely accept students based on their academic performance in secondary education. This approach ensures that the most qualified students, who have a solid foundation in the required academic subjects, are selected for college admission. It also eliminates any biases that may arise from other factors such as family connections or socioeconomic status. In the long run, this will lead to a better-educated population and a more competitive workforce. Therefore, I urge you to support this motion.
"""

# 'Welcome to Hackers Realm. It contains tutorial videos on technology'

# convert text to speech
text_to_speech = gTTS(text=text, lang='en', slow=False)

# save the audio file
text_to_speech.save('test_gtts.mp3')

# play the audio
playsound('test_gtts.mp3')