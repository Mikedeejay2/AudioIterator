import consumers
from file_iterator import FileIterator

if __name__ == '__main__':
    amplify_consumer = consumers.AmplifyConsumer(amplifier=1000)
    iterator = FileIterator("test", amplify_consumer)
    iterator.iterate_all()
