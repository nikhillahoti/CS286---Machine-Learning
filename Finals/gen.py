#pip3 install textgenrnn
#source: https://github.com/minimaxir/textgenrnn

from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.reset()
textgen.train_from_file('ZodiacWriting.txt', header=False, num_epochs=10)
textgen.generate_to_file('dummy.txt', n=50)
