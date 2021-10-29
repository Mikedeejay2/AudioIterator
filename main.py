import consumers
from file_iterator import FileIterator

if __name__ == '__main__':
    amplify_consumer = consumers.AmplifyConsumer(amplifier=1000)
    reverse_consumer = consumers.ReverseConsumer()
    append_consumer = consumers.AppendRandom("other", volume=-12)
    mono_consumer = consumers.MonoConsumer()
    iterator = FileIterator("test", mono_consumer)
    iterator.iterate_all()
