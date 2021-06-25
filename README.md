# AudioIterator
A simple script for quickly manipulating a large amount of audio using Python.

### Features
* Amplify audio
* Reverse audio
* Append a random audio file to another audio file

### Motives
This script was quickly put together so I could amplify a large amount of audio files. Now it can also 
reverse audio and append a random audio file to another audio file. It's super simple and probably not
well put together but it's great for what it was used for.

### How to use
Check `main.py` and look around. All audio consumers are kept inside of `consumers.py` which also means
that adding new audio consumers isn't difficult and can be easily copy and pasted to create a new consumer.
An input folder must be specified to the consumer being used, sometimes other arguments, and then the
`FileIterator` does the work iterating through the files and activating the consumer using 
`iterator.iterate_all()`.
