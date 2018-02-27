import time
import math
import pickle
import random
import numpy


start = time.time()

pickle_in = open("brownUnigrams.pickle", "rb")
Unigrams = pickle.load(pickle_in)

pickle_in = open("brownBigrams.pickle", "rb")
Bigrams = pickle.load(pickle_in)

pickle_in = open("brownTrigrams.pickle", "rb")
Trigrams = pickle.load(pickle_in)

print("Pickle in time:" + str(time.time() - start))

choices = {}
sent = ['<s>']
for key2, val2 in Bigrams.items():
    bigram = key2.split()
    if bigram[0] == "<s>":
        choices[bigram[1]] = math.pow(10, val2)
nextWord = numpy.random.choice(list(choices.keys()), p=list(choices.values()))
sent.append(nextWord)
print(sent)
while not(sent[-1] == "<\s>"):
    start = time.time()
    success = 0
    prevWord1 = str(sent[-1])
    prevWord2 = str(sent[-2])
    try:
        choices = {key3.split()[2]: math.pow(10, val3) for key3, val3 in Trigrams.items() if (prevWord2 + " " + prevWord1 + " ") in key3}
        success = 1
    except:
        # print("Trigram failed")
        continue
    # print("Trigram try: " + str(time.time() - start))

    if success == 0:
        try:
            choices = {key2.split()[1]: math.pow(10, val2) for key2, val2 in Bigrams.items() if
                   (prevWord1 + " ") in key2}
            success = 1
        except:
            # print("Bigram failed")
            continue
        # print("Bigram try: " + str(time.time() - start))
    if success == 0:
        for key1, val1 in Unigrams.items():
            choices[key1] = math.pow(10, val1)
        # print("Unigram try: " + str(time.time() - start))
    try:
        nextWord = random.choices(list(choices.keys()), weights=list(choices.values()))
    except ValueError:
        weights = list(choices.values())
        normWeights = [float(i) / sum(weights) for i in weights]
        nextWord = random.choices(list(choices.keys()), weights=normWeights)

    sent.append(str(nextWord[0]))
    # print(time.time() - start)

print(' '.join(sent))
