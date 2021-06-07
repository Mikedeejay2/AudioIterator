import os

import util


class FileIterator:
    def __init__(self, path, consumer):
        self.path = path
        self.consumer = consumer

    def iterate_all(self):
        for root, dirs, files in os.walk(self.path):
            for name in files:
                path = os.path.join(root, name)
                if util.get_snd_format(path) is None:
                    continue
                self.consumer.consume(path)
