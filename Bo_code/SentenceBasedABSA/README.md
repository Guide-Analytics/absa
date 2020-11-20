# Intro

There are 5 iPython notebooks in this repo.
1. Sentence_Partition matches sentences into aspects. The output of this notebook is used for sentiment analysis in notebook 2~4.
2. Sentiment analysis-Vader perform sentiment analysis on the sentence level using the Vader classifier from NLTK. This is a rule-based approach. The drawback is that the output will always be 3 classes. ([for more details](https://www.nltk.org/_modules/nltk/sentiment/vader.html))
3. Sentiment analysis-Textblob-Naive Bayes perform sentiment analysis on the sentence level using the **Naive Bayes** classifier from Textblob. The classifier is trained on a movie review dataset. ([for more details](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.en.sentiments.NaiveBayesAnalyzer))
4. Sentiment analysis-Textblob-Pattern perform sentiment analysis on the sentence level using the Pattern Analyzer classifier from Textblob. ([for more details](https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.en.sentiments.PatternAnalyzer))
5. ABSA pipeline performs ABSA on the product level. (Combines notebook 1 and 4). The output is a table of size (# of products) * (# of aspects + product information needed)

Other documents:
* product_level_ABSA.csv is the output of notebook 5.
* requirements.txt specify the library versions to run notebook 5.

For future improvement:
* To change the sentiment classifier, update the function *find_sentiment(sentence)* in notebook 5.