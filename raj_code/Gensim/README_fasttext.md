# Fasttext Word Embeddings

## Overview

Unlike word2vec, Fasttext looks for ngram of the target word.
It is useful in applications like spelling corrections where words that are similar to the typed word.

For instance, words like <em>Gide</em> and <em>Guide</em> are similar in the context of their characters.

More readings: https://amitness.com/2020/06/fasttext-embeddings/

## Parameters

One of the important parameters are:

* size: Dimension of the word vectors/embeddings. <br>
* window: number of characters/words considered before and after the target word.<br>
  * For example, consider a sentence, "I purchased this product in least price." with target word <em>product</em>.
    The character ngram for the target word: 
    ["pu","ur","ch","ha","as","se","ed"]
   * <em>Note: word2vec only performs the windowing on neighbouring words.</em>
* min_count: It discards the words with frequency less than the min_count value. Hence, it prevents the rare words taken into consideration and also helps to reduce the memory.

You can find more parameters and model information here: https://radimrehurek.com/gensim/models/fasttext.html
Default parameter values are described here: https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#:~:text=In%20addition%2C%20fastText%20has%20three,for%20hashing%20ngrams%20(Default%202000000)

Note: Results of any kind of embeddings is highly dependent on the preprocessing of the text.

Cons:
* Finding contextual information


