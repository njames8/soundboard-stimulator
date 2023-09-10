from .base_tones import Notes, Tone
from .scales import Scale

class Chord:
    def __init__(self, key: Scale, chord_root: Notes):
        self._key = key
        self._root_note = chord_root

    @property
    def notes(self) -> [Notes]:
        scale_notes = self._key.notes
        len_scale_notes = len(scale_notes)
        scale_index = scale_notes.index(self._root_note)
        result = [self._root_note]

        while len(result) < 4:
            if scale_index + 2 < len_scale_notes:
                scale_index += 2
            else:
                scale_index = 2 - (len_scale_notes - scale_index)

            result.append(scale_notes[scale_index])
        print(result)
        return result

class ChordTone:
    def __init__(self, chord: Chord, octave: int):
        self._chord = chord
        self._octave = octave

    @property
    def tones(self) -> [Tone]:
        notes = self._chord.notes
        root = notes[0]
        result = []
        for note in notes:
            octave = self._octave if note.value >= root.value else self._octave + 1
            result.append(Tone(note=note, octave=octave))

        return result