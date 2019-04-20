# Contexts to Categories

> Creates a list of contexts and words that occur in that context, as well as the number of times a word occurs in a given context, from the Brown Corpus (via NLTK).

This script was produced using Python 3.7.2.

This code operates under the following steps:

1. Import the Brown Corpus using NLTK (note that this contains 1.15M words as opposed to the 235K-word slice provided by Prof. Goldsmith).
2. Get all sentences from the Brown Corpus and lowercase them, stored in `lowered_sents`.
3. Create dictionary `contexts` for contexts.
4. Get pairs of three words for each sentence in `lowered_sents` using `nltk.trigrams`.
5. For each pair of trigrams add the context of the format `wd1 ___ wd3`, as well as a subdictionary for each context containing the words that occur in that context, along with the number of times that word occurs in that context to `contexts`.
6. Create a dictionary `num_words_per_context` that will store each context and the total number of *unique* words that appear in that context.
7. For each context, add the number of unique words as that context's value in the `num_words_per_context` dict.
8. Sort the `num_words_per_context` dict by values, descending.
9. Create a dictionary `sorted_wic` that will store each context in `contexts` with its values sorted by total number of occurrences (descending) in that context.
10. Sort the values of each context by number of occurrences (descending) and add them to the `sorted_wic` dict.
11. For each context sorted by number of unique words per context, if there are more than 50 unique words, print the context and the number of words to `context_list.txt`.
12. Print each context with more than 50 unique words to `words_in_contexts.txt` as well as the words that occur in that context and the number of times that word occurs. 5 words per line.

# Thought Questions Responses

1. **Consider the first context on your list, which is "the ___ of". Are these words all of the same category? Are there exceptions to that? Are there any particular sort of words of that category that appear here?**

  - There are a great number of nouns. I'm sure there are a small number of words of other categories, however I can't seem to find any (which exemplifies how few there are, if any).

2. **The second context is "the ___ .". Are these words all of the same category? Why are there some odd things showing up, like *u*? Is *u* even a word? Where did it come from? Is “.” ambiguous, and does that have an impact on these results? What impact?**

  - Again, a lot of these words are of category N. "." is ambiguous and could have effects on acronyms, like "the U.S.A.", which could potentially be where the puzzling "u" in this question comes from.

3. **The third context is ", ___ ,". Are these words of the same category? Why or why not? Does this relate to anything about the use of the comma?**

 - This context tends to have more of a mixup of categories of words. I see a lot of adverbs like "however" and "ultimately", a number of verbs like "implements" or "implying", some adjectives like "ankle-deep" and "broad", and of course lots of nouns.

4. **Sometimes we have expressions like *of course* which act more like a single word even though we spell them as two words. Such expressions can be found (so to speak) in a context such as "of ___ ,". Can you find other examples like that?**

  - "Of all" occurs pretty high in the list. I would expect to see something like "of interest", but can't seem to find it in the list.

5. **As you look, you will find quite a few contexts which seem to select for nouns. Is there a large overlap between the nouns that each context has identified? Does this lead to a method you could use to analyze a language which you did not actually know?**

  - It's a little hard to tell, but there are definitely some high frequency words across contexts. In particular, I see a lot of pronouns. These tend to be similar to one another cross-linguistically (and language family-internally), so it'd probably be easy to spot some of the pronouns when looking at a new language.

6. ** *fig* is not a common word in English, and yet it appears in several of the contexts. Why is that?**

  - It probably stands for *figure*.

7. **What contexts find verbs? What contexts find adjectives? How about singular nouns and plural nouns? Parts of the body? Family members?**

  - Verbs are usually found preceding *to* or following a word of category N. Nouns are usually found after determiners. Adjectives tend to come after inflected forms of *be*. Parts of the body after possessive pronouns; same for family members.
