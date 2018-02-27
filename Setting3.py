import time
import math
import pickle
import random
import numpy
from nltk.corpus import brown

# no of words in brown = 1161192
# no of words in brownTest = 181530
# no of words in brownTrain = 979662
# print(len(brown.sents())) = 57340 45872
# print(len(gutenberg.sents())) = 98552 78841
# no of words in gutenberg = 2621613
# no of words in gutenbergTest = 513303
# no of words in gutenbergTrain = 2108310

start = time.time()

pickle_in = open("gutenbergBrownUnigrams.pickle", "rb")
Unigrams = pickle.load(pickle_in)

pickle_in = open("gutenbergBrownBigrams.pickle", "rb")
Bigrams = pickle.load(pickle_in)

pickle_in = open("gutenbergBrownTrigrams.pickle", "rb")
Trigrams = pickle.load(pickle_in)

# print("Pickle in time:" + str(time.time() - start))

# # TEST MODULE - outputs perplexity # #
start = time.time()
totPerplexity = 0
iterCount = 0
for sent in brown.sents()[45873:]:
    probOfSent = 0
    sent.insert(0, "<s>")
    sent.append("<\s>")
    prev_word2 = sent[0]
    word = sent[1]
    try:
        probOfSent += Bigrams[prev_word2 + " " + word]
    except KeyError:
        probOfSent += -6
    prev_word1 = sent[0]
    prev_word2 = sent[1]
    for word in sent[2:]:
        try:
            trigram = prev_word1 + " " + prev_word2 + " " + word
            if trigram in Trigrams:
                probOfSent += Trigrams[trigram]
            elif (prev_word2 + " " + word) in Bigrams:
                probOfSent += Bigrams[prev_word2 + " " + word]
            else:
                probOfSent += Unigrams[word]
        except KeyError:
            probOfSent += (-6.35)
        prev_word1 = prev_word2
        prev_word2 = word
    try:
        perplexity = math.pow(1/(math.pow(10, probOfSent)), 1/len(sent))
        if perplexity == float('inf'):
            iterCount += 1
            # print(perplexity)
        else:
            totPerplexity += perplexity
    except ZeroDivisionError:
        iterCount += 1
        # print(math.pow(10, probOfSent))
        # print(len(sent))

print("No of ZeroDivisionErrors: " + str(iterCount))
print("Total Perplexity: " + str(totPerplexity))
avgPerplexity = totPerplexity/(len(brown.sents()[45873:]) - iterCount)
print("Avg Perplexity = " + str(avgPerplexity))
print("Perplexity time: " + str(time.time() - start))

# choices = {}
# sent = ['<s>']
# for key2, val2 in Bigrams.items():
#     bigram = key2.split()
#     if bigram[0] == "<s>":
#         choices[bigram[1]] = math.pow(10, val2)
# nextWord = numpy.random.choice(list(choices.keys()), p=list(choices.values()))
# sent.append(nextWord)
# print(sent)
# while not(sent[-1] == "<\s>"):
#     start = time.time()
#     success = 0
#     prevWord1 = str(sent[-1])
#     prevWord2 = str(sent[-2])
#     try:
#         choices = {key3.split()[2]: math.pow(10, val3) for key3, val3 in Trigrams.items() if (prevWord2 + " " + prevWord1 + " ") in key3}
#         success = 1
#     except:
#         print("Trigram failed")
#         continue
#     # print("Trigram try: " + str(time.time() - start))
#
#     if success == 0:
#         try:
#             choices = {key2.split()[1]: math.pow(10, val2) for key2, val2 in Bigrams.items() if
#                    (prevWord1 + " ") in key2}
#             success = 1
#         except:
#             print("Bigram failed")
#             continue
#         print("Bigram try: " + str(time.time() - start))
#     if success == 0:
#         for key1, val1 in Unigrams.items():
#             choices[key1] = math.pow(10, val1)
#         print("Unigram try: " + str(time.time() - start))
#     try:
#         nextWord = random.choices(list(choices.keys()), weights=list(choices.values()))
#     except ValueError:
#         weights = list(choices.values())
#         normWeights = [float(i) / sum(weights) for i in weights]
#         nextWord = random.choices(list(choices.keys()), weights=normWeights)
#
#     sent.append(str(nextWord[0]))
#     # print(time.time() - start)
#
# print(' '.join(sent))
