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
    def __init__(self):
        super().__init__()
        self.number = 0

    def consume(self, path=""):
        if path.endswith(".ogg"):
            print(path)
            loop = AudioSegment.from_ogg(path)
            play(loop)
