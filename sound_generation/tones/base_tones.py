from enum import Enum
from math import pow, trunc

class Notes(Enum):
    C = 0
    C_SHARP = 1
    D = 2
    D_SHARP = 3
    E = 4
    F = 5
    F_SHARP = 6
    G = 7
    G_SHARP = 8
    A = 9
    A_SHARP = 10
    B = 11

    @property
    def relation_to_a(self) -> int:
        return self - Notes.A
    
class Tone:
    FREQUENCY_CONSTANT = 1.059463094359
    A4_FREQUENCY = 440.0

    def __init__(self, note: Notes, octave: int):
        if octave < 0 or octave > 8: raise ValueError
        self._note = note
        self._octave = octave

    @property
    def note(self) -> Notes:
        return self._note
    
    @property
    def octave(self) -> int:
        return self._octave

    @property
    def frequency(self) -> float:
        return trunc(Tone.A4_FREQUENCY * pow(Tone.FREQUENCY_CONSTANT, self.note.relation_to_a), 2)