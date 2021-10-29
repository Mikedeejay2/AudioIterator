from abc import ABC, abstractmethod
from pydub import AudioSegment
import util
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
        sound = util.get_sound(path)
        amplified_sound = sound + self.amplifier
        util.export(amplified_sound, path)


class ReverseConsumer(Consumer):
    def consume(self, path=''):
        sound = util.get_sound(path)
        reversed_sound = sound.reverse()
        util.export(reversed_sound, path)


class AppendRandom(Consumer):
    def __init__(self, other_path='', volume=0, position=0):
        super().__init__()
        self.other_path = other_path
        self.volume = volume
        self.position = position

    def consume(self, path=''):
        sound = util.get_sound(path)
        sound2 = util.get_random_sound(self.other_path)
        sound2 = sound2 + self.volume
        added_sound: AudioSegment
        if sound.duration_seconds > sound2.duration_seconds:
            added_sound = sound.overlay(sound2, position=self.position)
        else:
            added_sound = sound2.overlay(sound, position=self.position)
        util.export(added_sound, path)


class MonoConsumer(Consumer):
    def consume(self, path=''):
        sound = util.get_sound(path)
        mono_sound = sound.set_channels(1)
        util.export(mono_sound, path)
