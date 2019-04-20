import nltk
from nltk.corpus import brown
from collections import OrderedDict

# Get all sentences in Brown Corpus.
sents = brown.sents()
lowered_sents = []

# Lowercase each sentence and append it to `lowered_sents`.
for sent in sents:
    lowered_sent = [w.lower() for w in sent]
    lowered_sents.append(lowered_sent)

# Create dictionary for contexts.
contexts = {}

# Get pairs of three words (trigrams) for each sentence in `lowered_sents`.
tris = [list(nltk.trigrams(s)) for s in lowered_sents]

# For each pair of trigrams add the context as well as
# the words that occur in that context along with
# the number of times that word occurs in that context.
for sent in tris:
    for w1, w2, w3 in sent:
        context = f'{w1} ___ {w3}'

        # If the context is not already in the `contexts` dictionary, add it.
        if context not in contexts:
            contexts[context] = {w2: 1}

        # If the context is already in the `contexts` dictionary,
        # and the word is already listed as being in that context,
        # add 1 to the number of occurrences of that word in the context.
        else:
            if w2 in contexts[context]:
                contexts[context][w2] += 1

            # Otherwise, add the word as a value of the context in `contexts`
            # and give it a number of occurrences of 1.
            else:
                contexts[context][w2] = 1

# Create a dictionary that will store each context
# and the number of *unique* words that appear in that context.
num_words_per_context = {}

# For each context, add the number of unique words as that context's value
# in the `num_words_per_context` dict.
for c in contexts:
    for wd in contexts[c]:
        if c not in num_words_per_context:
            num_words_per_context[c] = 1
        else:
            num_words_per_context[c] += 1

# Sort the `num_words_per_context` dict by values, descending.
sorted_nwpc = OrderedDict(sorted(num_words_per_context.items(), key=lambda kv: kv[1], reverse=True))

# Create a dictionary that will store each context in `contexts`
# with its values sorted by total number of occurrences (descending)
# in that context.
sorted_wic = {}

# Sort the values of each context by number of occurrences (descending)
# and add them to the `sorted_wic` dict.
for c in contexts:
    srtd = sorted(contexts[c].items(), key=lambda kv: kv[1], reverse=True)
    sorted_wic[c] = srtd

# Open each file and append necessary information.
with open('context_list.txt', 'w') as cl, open('words_in_contexts.txt', 'w') as wic:

    # For each context sorted by number of unique words per context,
    # if there are more than 50 unique words,
    # print the context and the number of words to `context_list.txt`.
    for c in sorted_nwpc:
        if sorted_nwpc[c] >= 50:
            cl.write(f'{c}: {sorted_nwpc[c]} \n\n')

            # For each of these contexts, print it
            # to `words_in_contexts.txt`.
            wic.write(f'Context: {c}\nWords and occurrences:\n')

            i = 0
            for wd, occ in sorted_wic[c]:
                wic.write(f'  {wd}: {occ}; ')
                i += 1

                # Print 5 words that appear in the context per line.
                if i % 5 == 0:
                    wic.write('\n')

                # If the counter `i` reaches the length of the number of
                # words in the context, print two line breaks.
                # This is to create a space between context/word lists
                # in the output file.
                elif i == len(sorted_wic[c]):
                    wic.write('\n\n')
