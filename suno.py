from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

preload_models()

# generate audio from text
text_prompt = """
I strongly believe that college entrance examinations should solely accept students based on their academic performance in secondary education. This approach ensures that the most qualified students, who have a solid foundation in the required academic subjects, are selected for college admission. It also eliminates any biases that may arise from other factors such as family connections or socioeconomic status. In the long run, this will lead to a better-educated population and a more competitive workforce. Therefore, I urge you to support this motion.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)