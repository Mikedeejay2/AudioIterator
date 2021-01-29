import os


class FileIterator:
    def __init__(self, path, consumer):
        self.path = path
        self.consumer = consumer

    def iterate_all(self):
        for root, dirs, files in os.walk(self.path):
            for name in files:
                self.consumer.consume(os.path.join(root, name))
