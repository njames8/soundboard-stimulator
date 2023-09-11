import argparse
from sound_generation.tones.base_tones import Tone, Notes
from sound_generation.sound_generator import play

def default(duration: float):
    tones = [
        Tone(note=Notes.E, octave=2), 
        Tone(note=Notes.A, octave=2),
        Tone(note=Notes.D, octave=3),
        Tone(note=Notes.G, octave=3),
        Tone(note=Notes.B, octave=3),
        Tone(note=Notes.E, octave=4)
    ]
    play(tones=tones, duration_seconds=duration)

def parse_notes(notes_str: str) -> [Tone]:
    notes_list = notes_str.split(',')
    tones = []
    for note_str in notes_list:
        note, octave_str = note_str.split(':')
        note = Notes(note)
        tones.append(Tone(Notes(note), int(octave_str)))
    return tones

def convert_hours_to_seconds(hours: float) -> int:
   return int(hours * 60 * 60)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Soundboard Stimulator',
        description='Generates sound to break in wooden instruments\' soundboards')
    parser.add_argument('-n', '--notes', dest='notes', type=parse_notes, required=False)
    parser.add_argument('-d', '--duration', dest='duration', type=float, required=True, help='The length of time in hours to stimulate the soundboard')
    args = parser.parse_args()

    duration = convert_hours_to_seconds(args.duration)
    if args.notes == None:
        default(duration)
    else:
        play(tones=args.notes, duration_seconds=duration)
