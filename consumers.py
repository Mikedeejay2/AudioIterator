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
    def consume(self, path=""):
        if not path.endswith(".ogg"):
            loop = AudioSegment.from_ogg(path)
            play(loop)
