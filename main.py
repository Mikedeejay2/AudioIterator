import consumers, file_iterator


if __name__ == '__main__':
    amplify_consumer = consumers.AmplifyConsumer()
    iterator = file_iterator.FileIterator("test", amplify_consumer)
    iterator.iterate_all()
