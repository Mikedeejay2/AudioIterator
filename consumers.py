from abc import ABC, abstractmethod


class Consumer:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def consume(self, path):
        pass


class AmplifyConsumer(Consumer):
    def consume(self, path):
        print(path)
