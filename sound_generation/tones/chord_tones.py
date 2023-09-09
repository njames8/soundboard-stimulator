from .base_tones import Notes
from enum import Enum

class ScalesTypes(Enum):
    MAJOR = [2, 2, 1, 2, 2, 2]
    MINOR = [2, 1, 2, 2, 1, 2]

class Scale:
    def __init__(self, root: Notes, scale_type: ScalesTypes):
        self._root = root
        self._scale_type = scale_type

    @property
    def notes(self) -> [Notes]:
        current_note = self._root
        scale_notes = [current_note]

        number_of_notes = len(Notes)
        scale_index = 0
        note_index = current_note.value

        while scale_index < len(self._scale_type.value):
            number_of_steps = self._scale_type.value[scale_index]
            if note_index + number_of_steps < number_of_notes:
                note_index += number_of_steps
            else:
                note_index = number_of_steps - (number_of_notes - note_index)
            
            scale_notes.append(Notes(note_index))
            scale_index += 1
        
        return scale_notes
            