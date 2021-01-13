# word2vec Word Embeddings

## Overview

Unlike word2vec, Fasttext looks for ngram of the target word.
It is useful in applications like spelling corrections where words that are similar to the typed word.

For instance, words like <em>Gide</em> and <em>Guide</em> are similar in the context of their characters.

More readings: https://radimrehurek.com/gensim/models/word2vec.html

## Parameters

One of the important parameters are:

* size: Dimension of the word vectors/embeddings. <br>
* window: number of characters/words considered before and after the target word.<br>
  * For example, consider a sentence, "I purchased this product in least price." with target word <em>product</em>.
    The character ngram for the target word: 
    ["purchased","this","in","least"]
* min_count: It discards the words with frequency less than the min_count value. Hence, it prevents the rare words taken into consideration and also helps to reduce the memory.

Note: Results of any kind of embeddings is highly dependent on the preprocessing of the text.

Cons:
* Finding contextual information
* Look at neighbouring words and not the target character window that can help to relate singular and plural words as well.
    * Look for Fasttext.