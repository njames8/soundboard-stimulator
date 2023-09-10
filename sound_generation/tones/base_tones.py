from enum import Enum
from math import pow, trunc
from typing import Any

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
        
    @classmethod
    def parse_str(cls, string):
        lowercased = string.lower()
        if lowercased == 'c' or lowercased == 'b#':
            return Notes.C.value
        elif lowercased == 'c#' or lowercased == 'db':
            return Notes.C_SHARP.value
        elif lowercased == 'd':
            return Notes.D.value
        elif lowercased == 'd#' or lowercased == 'eb':
            return Notes.D_SHARP.value
        elif lowercased == 'e' or lowercased == 'fb':
            return Notes.E.value
        elif lowercased == 'f' or lowercased == 'e#':
            return Notes.F.value
        elif lowercased == 'f#' or lowercased == 'gb':
            return Notes.F_SHARP.value
        elif lowercased == 'g':
            return Notes.G.value
        elif lowercased == 'g#' or lowercased == 'ab':
            return Notes.G_SHARP.value
        elif lowercased == 'a':
            return Notes.A.value
        elif lowercased == 'a#' or lowercased == 'bb':
            return Notes.A_SHARP.value
        elif lowercased == 'b' or lowercased == 'cb':
            return Notes.B.value
        else:
            return super()._missing_(string)
        
    @classmethod
    def _missing_(cls, value: object) -> Any:
        if isinstance(value, str):
            return cls(Notes.parse_str(value))
        else:
            return super()._missing_(value)

    @property
    def relation_to_a(self) -> int:
        return self.value - Notes.A.value
    
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
        relation_to_a =  self.note.relation_to_a + (12 * (self._octave - 4))
        new_frequency_coefficient = pow(Tone.FREQUENCY_CONSTANT, relation_to_a)
        result = round(Tone.A4_FREQUENCY * new_frequency_coefficient, 2)
        return result
    
class Overtone:
    def __init__(self, tone: Tone):
        self._tone = tone

    def foundational(self) -> (Tone, float):
        self._tone

    def first_degree(self) -> (Tone, float):
        return (Tone(self._tone.note, self._tone.octave + 1), 0.25)

    def second_degree(self) -> (Tone, float):
        fifth = (self._tone.note.value + 7) % 12
        new_octave = self._tone.octave + 1 if fifth < self._tone.note.value else self._tone.octave
        return (Tone(Notes(fifth), new_octave + 1), 0.1111)
    
    def third_degree(self) -> (Tone, float):
        return (Tone(self._tone.note, self._tone.octave + 2), 0.0625)
    
    def fourth_degree(self) -> (Tone, float):
        third = (self._tone.note.value + 4) % 12
        new_octave = self._tone.octave + 1 if third < self._tone.note.value else self._tone.octave
        return (Tone(Notes(third), new_octave + 2), 0.04)