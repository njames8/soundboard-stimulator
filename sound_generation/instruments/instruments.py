from tones.base_tones import Tone, Notes
from enum import Enum

class Instrument:
    def __init__(self, name: str, lowest_tone: Tone, highest_tone: Tone, max_oscs: int):
        self._name = name
        self._lowest_tone = lowest_tone
        self._highest_tone = highest_tone
        self._max_oscs = max_oscs

    @property
    def name(self):
        return self._name

    @property
    def lowest_tone(self):
        return self._lowest_tone
    
    @property
    def highest_tone(self):
        return self._highest_tone
    
    @property
    def max_oscs(self):
        return self._max_oscs

class Instruments(Enum):
    GUITAR_STANDARD_TUNING_22_FRET = Instrument('Guitar Standard Tuning 22 Fret', Tone(Notes.E, 2), Tone(Notes.D, 5), 6)
