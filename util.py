import os
import random

from pydub import AudioSegment


def get_sound_wpath(path='', snd_format=''):
    print(path)
    if snd_format == 'ogg':
        return AudioSegment.from_ogg(path)
    elif snd_format == 'mp3':
        return AudioSegment.from_mp3(path)
    elif snd_format == 'wav':
        return AudioSegment.from_wav(path)
    elif snd_format == 'flv':
        return AudioSegment.from_flv(path)


def get_snd_format(path=''):
    if path.endswith('.ogg'):
        return 'ogg'
    elif path.endswith('.mp3'):
        return 'mp3'
    elif path.endswith('.wav'):
        return 'wav'
    elif path.endswith('.flv'):
        return 'flv'


def get_sound(path=''):
    return get_sound_wpath(path, get_snd_format(path))


def export(segment: AudioSegment, path=''):
    segment.export(path, format=get_snd_format(path))


def get_random_file(path=''):
    return random.choice(os.listdir(path))


def get_random_sound(path=''):
    file = os.path.join(path, get_random_file(path))
    return get_sound(file)
