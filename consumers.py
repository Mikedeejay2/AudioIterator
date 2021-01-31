from abc import ABC, abstractmethod
from pydub import AudioSegment
from pydub.playback import play


class Consumer(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def consume(self, path=""):
        pass


class PrintDirConsumer(Consumer):
    def consume(self, path=""):
        print(path)


class AmplifyConsumer(Consumer):
    def __init__(self, amplifier=0):
        super().__init__()
        self.amplifier = amplifier

    def consume(self, path=''):
        snd_format = ''
        sound: AudioSegment
        if path.endswith('.ogg'):
            snd_format = 'ogg'
            sound = AudioSegment.from_ogg(path)
        if snd_format == '':
            return
        print(path)
        amplified_sound = sound + self.amplifier
        amplified_sound.export(path, format=snd_format)


class ReverseConsumer(Consumer):
    def consume(self, path=''):
        snd_format = ''
        sound: AudioSegment
        if path.endswith('.ogg'):
            snd_format = 'ogg'
            sound = AudioSegment.from_ogg(path)
        if snd_format == '':
            return
        print(path)
        reversed_sound = sound.reverse()
        reversed_sound.export(path, format=snd_format)
