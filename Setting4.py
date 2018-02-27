import time
import math
import pickle
import random
import numpy
from nltk.corpus import gutenberg
from nltk.corpus import brown


# no of words in brown = 1161192
# no of words in brownTest = 181530
# no of words in brownTrain = 979662
# print(len(brown.sents())) = 57340 45872
# print(len(gutenberg.sents())) = 98552 78841
# no of words in gutenberg = 2621613
# no of words in gutenbergTest = 513303
# no of words in gutenbergTrain = 2108310


## THIS CODE CAN BE UNCOMMENTED FOR TRAINING. ##
## THE TRAINED MODEL IS LOADED THROUGH PICKLE ##
# start = time.time()
# Unigrams = {}
#
# # loop over unigrams:
# for word in gutenberg.words()[:2108310]:
#     if word in Unigrams:
#         Unigrams[word] += 1
#     else:
#         Unigrams[word] = 1
#
# for word in brown.words()[:979662]:
#     if word in Unigrams:
#         Unigrams[word] += 1
#     else:
#         Unigrams[word] = 1
# Unigrams["<s>"] = 78841 + 45872
# Unigrams["<\s>"] = 78841 + 45872
#
# # # Write unigrams to output file:
# # output_file = open("unigrams.txt", "w")
# # for unigram in Unigrams:
# #     count = Unigrams[unigram]
# #     output_file.write(str(count) + "\t" + unigram + "\n")
# # output_file.close()
# print("Unigram time: " + str(time.time() - start))
# start = time.time()
#
# # initialize variables:
# Bigrams = {}
#
# for sent in gutenberg.sents()[:78841]:
#     prev_word = "<s>"
#     # loop over words in input:
#     for word in sent:
#         # concatenate words to get bigram:
#         bigram = prev_word + " " + word
#         if bigram in Bigrams:
#             Bigrams[bigram] += 1
#         else:
#             Bigrams[bigram] = 1
#         # change value of prev_word
#         prev_word = word
#     bigram = prev_word + " <\s>"
#     if bigram in Bigrams:
#         Bigrams[bigram] += 1
#     else:
#         Bigrams[bigram] = 1
#
# for sent in brown.sents()[:45872]:
#     prev_word = "<s>"
#     # loop over words in input:
#     for word in sent:
#         # concatenate words to get bigram:
#         bigram = prev_word + " " + word
#         if bigram in Bigrams:
#             Bigrams[bigram] += 1
#         else:
#             Bigrams[bigram] = 1
#         # change value of prev_word
#         prev_word = word
#     bigram = prev_word + " <\s>"
#     if bigram in Bigrams:
#         Bigrams[bigram] += 1
#     else:
#         Bigrams[bigram] = 1
#
#
# # output_file = open("bigrams.txt","w")
# # for bigram in Bigrams:
# #     count = Bigrams[bigram]
# #     output_file.write(str(count)+ "\t" + bigram + "\n" )
# # output_file.close()
# print("Bigram time: " + str(time.time() - start))
#
# start = time.time()
# # initialize variables:
# Trigrams = {}
#
# for sent in gutenberg.sents()[:78841]:
#     #print(sent)
#     #print(sent[1])
#     prev_word1 = "<s>"
#     prev_word2 = sent[0]
#     # loop over words in input:
#     for word in sent[1:]:
#         # concatenate words to get trigram:
#         trigram = prev_word1 + " " + prev_word2 + " " + word
#         if trigram in Trigrams:
#             Trigrams[trigram] += 1
#         else:
#             Trigrams[trigram] = 1
#         # change value of prev_word
#         prev_word1 = prev_word2
#         prev_word2 = word
#     trigram = prev_word1 + " " + prev_word2 + " <\s>"
#     if trigram in Trigrams:
#         Trigrams[trigram] += 1
#     else:
#         Trigrams[trigram] = 1
#
# for sent in brown.sents()[:45871]:
#     #print(sent)
#     #print(sent[1])
#     prev_word1 = "<s>"
#     prev_word2 = sent[0]
#     # loop over words in input:
#     for word in sent[1:]:
#         # concatenate words to get bigram:
#         trigram = prev_word1 + " " + prev_word2 + " " + word
#         if trigram in Trigrams:
#             Trigrams[trigram] += 1
#         else:
#             Trigrams[trigram] = 1
#         # change value of prev_word
#         prev_word1 = prev_word2
#         prev_word2 = word
#     trigram = prev_word1 + " " + prev_word2 + " <\s>"
#     if trigram in Trigrams:
#         Trigrams[trigram] += 1
#     else:
#         Trigrams[trigram] = 1
# print("Trigram time: " + str(time.time() - start))
#
# start = time.time()
# iterCount = 0
# # output_file = open("trigrams.txt", "w")
# for key3, val3 in Trigrams.items():
#     iterCount += 1
#     # print(iterCount)
#     trigram = key3.split()
#     bigram = trigram[0] + " " + trigram[1]
#     Trigrams[key3] = math.log10(Trigrams[key3]/Bigrams[bigram])
# #     output_file.write(str(Trigrams[key3]) + "\t" + key3 + "\n")
# # output_file.close()
#
# iterCount = 0
# # output_file = open("bigrams.txt", "w")
# for key2, val2 in Bigrams.items():
#     iterCount += 1
#     # print(iterCount)
#     bigram = key2.split()
#     unigram = bigram[0]
#     try:
#         Bigrams[key2] = math.log10(Bigrams[key2]/Unigrams[unigram])
#     except KeyError:
#         Bigrams[key2] = -5
# #     output_file.write(str(Bigrams[key2]) + "\t" + key2 + "\n")
# # output_file.close()
#
# iterCount = 0
# totProb = 0
# # print(len(Unigrams))
# noOfWords = 979662 + 2108310
# # output_file = open("unigrams.txt", "w")
# for key1, val1 in Unigrams.items():
#     iterCount += 1
#     # print(iterCount)
#     Unigrams[key1] = math.log10(Unigrams[key1]/noOfWords)
#     totProb += math.pow(10, Unigrams[key1])
# #     output_file.write(str(Unigrams[key1]) + "\t" + key1 + "\n")
# # output_file.close()
# print("Total Unigram prob: " + str(totProb))
# print("LogProb time: " + str(time.time() - start))
#
# start = time.time()
#
# pickle_out = open("gutenbergBrownUnigrams.pickle", "wb")
# pickle.dump(Unigrams, pickle_out)
# pickle_out.close()
#
# pickle_out = open("gutenbergBrownBigrams.pickle", "wb")
# pickle.dump(Bigrams, pickle_out)
# pickle_out.close()
#
# pickle_out = open("gutenbergBrownTrigrams.pickle", "wb")
# pickle.dump(Trigrams, pickle_out)
# pickle_out.close()
#
# print("Pickle time:" + str(time.time() - start))

start = time.time()

pickle_in = open("gutenbergBrownUnigrams.pickle", "rb")
Unigrams = pickle.load(pickle_in)

pickle_in = open("gutenbergBrownBigrams.pickle", "rb")
Bigrams = pickle.load(pickle_in)

pickle_in = open("gutenbergBrownTrigrams.pickle", "rb")
Trigrams = pickle.load(pickle_in)

print("Pickle in time:" + str(time.time() - start))

# # TEST MODULE - outputs perplexity # #
start = time.time()
totPerplexity = 0
iterCount = 0
for sent in gutenberg.sents()[78842:]:
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
avgPerplexity = totPerplexity/(len(gutenberg.sents()[78842:]) - iterCount)
print("Avg Perplexity = " + str(avgPerplexity))
print("Perplexity time: " + str(time.time() - start))
#
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
