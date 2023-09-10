from .tones.base_tones import Tone, Overtone
import pyaudio
import numpy as np
import functools
import operator

def __sine(frequency, length, rate):
  length = int(length * rate)
  factor = float(frequency) * (np.pi * 2) / rate
  return np.sin(np.arange(length) * factor)

def play(tones: [Tone], duration_seconds: int, refresh_rate: int = 44100):
    foundational = functools.reduce(
       operator.add, 
       map(
          lambda tone: __sine(tone.frequency, length=duration_seconds, rate=refresh_rate), 
          tones
       )
    )
    
    overtones = list(map(lambda tone: Overtone(tone), tones))

    first_degree_waves = functools.reduce(
       operator.add,
       map(
        lambda overtone: __sine(overtone[0].frequency, length=duration_seconds, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.first_degree(), overtones)
       )
    )

    second_degree_waves = functools.reduce(
       operator.add,
       map(
        lambda overtone: __sine(overtone[0].frequency, length=duration_seconds, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.second_degree(), overtones)
       )
    )

    third_degree_waves = functools.reduce(
       operator.add,
       map(
        lambda overtone: __sine(overtone[0].frequency, length=duration_seconds, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.third_degree(), overtones)
       )
    )

    fourth_degree_waves = functools.reduce(
       operator.add,
       map(
        lambda overtone: __sine(overtone[0].frequency, length=duration_seconds, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.fourth_degree(), overtones)
       )
    )

    wave = np.concatenate([
        foundational +
        first_degree_waves +
        second_degree_waves +
        third_degree_waves +
        fourth_degree_waves
    ]) * 0.1
    
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=refresh_rate, output=1)
    stream.write(wave.astype(np.float32).tobytes())
    stream.close()
    p.terminate()