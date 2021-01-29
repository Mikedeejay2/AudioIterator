from consumers import AmplifyConsumer
from file_iterator import FileIterator

if __name__ == '__main__':
    amplify_consumer = AmplifyConsumer()
    iterator = FileIterator("test", amplify_consumer)
    iterator.iterate_all()
