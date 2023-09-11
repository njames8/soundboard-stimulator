from .tones.base_tones import Tone, Overtone
import pyaudio
import numpy as np
import functools
import operator
import threading
import matplotlib.pyplot as plt
import math

def __sine(frequency, length, rate):
  duration = length * rate
  frequency_decimal = 1 - (frequency - math.floor(frequency))
  # non-integer frequencies don't perfectly end at zero. so here, we add the 
  # difference of where the frequency ends and zero to make a perfect wave
  # ex: C4 (middle c) has a frequency of 261.63Hz which creates a partial wave
  # at 2π. So we extend the wave by (1 - 0.63) cycles to create a perfect wave
  factor = (float(frequency) * (np.pi * 2) / rate) + ((frequency_decimal * 2 * np.pi) / rate)
  return np.sin(np.arange(duration) * factor)

def play(tones: [Tone], duration_seconds: int, refresh_rate: int = 44100):
    foundational = functools.reduce(
        operator.add, 
        map(
        lambda tone: __sine(tone.frequency, length=1, rate=refresh_rate), 
        tones
    )
    ) 

    overtones = list(map(lambda tone: Overtone(tone), tones))

    first_degree_waves = functools.reduce(
    operator.add,
    map(
        lambda overtone: __sine(overtone[0].frequency, length=1, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.first_degree(), overtones)
    )
    )

    second_degree_waves = functools.reduce(
    operator.add,
    map(
        lambda overtone: __sine(overtone[0].frequency, length=1, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.second_degree(), overtones)
    )
    )

    third_degree_waves = functools.reduce(
    operator.add,
    map(
        lambda overtone: __sine(overtone[0].frequency, length=1, rate=refresh_rate) * overtone[1],
        map(lambda overtone: overtone.third_degree(), overtones)
    )
    )

    fourth_degree_waves = functools.reduce(
    operator.add,
    map(
        lambda overtone: __sine(overtone[0].frequency, length=1, rate=refresh_rate) * overtone[1],
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

    converted_wave = wave.astype(np.float32).tobytes()
    thread = threading.Thread(target=play_sound, args=[duration_seconds, converted_wave, refresh_rate])
    thread.start()

def play_sound(duration, wave, refresh_rate):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=refresh_rate, output=1)
    
    for _ in range(duration):
        stream.write(wave)

    stream.close()
    p.terminate()
