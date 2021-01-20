# ASPECT BASED SENTIMENT ANALYSIS (ABSA) Rule Based Model.

## Overview

This approach identifies aspects and analysis corresponding sentiment WITHOUT any need of labelled data. At the most a corpus can be provided to ensure that some specific aspects are considered in case not picked up by the POS tagging.

Folder Contents:
1) *asba_ruleBased.ipynb* contains the main code.
2) *corpus.txt* contains the corpus of aspects. Currently, they are manually defined.
3) *pos.txt* and *neg.txt* contain positive and negative sentiment list.


## Introduction

Aspect Based Sentiment Analysis (ABSA) is a technique that takes into consideration the terms related to the aspects and identifies the sentiment associated with each aspect, rather than analysing sentiment at the review level. ABSA model requires aspect categories and its corresponding aspect terms to extract sentiment for each aspect from the text corpus. It is possible to create a domain-specific model for a specific implementation; though general language models can also be used.

Typical ABSA requires labeled data containing aspect terms and aspect categories for each statement along with its sentiment score. However, it can be solved using the unsupervised approach without having labeled data and a list of aspect terms. For example, what was the overall experience of customers with the restaurant staff, menu variety, price, taste, and location?

Thus, it becomes important to identify the aspects of the product/service that attract more customers and/or keep away people to use/buy the product/service. It can basically help in identifying what works and what not. ABSA identifies sentiment for each aspect category depending upon the business and/or the product. It helps business to track how end-users sentiment changes toward specific features and attributes of a service or product.

## Process

Firstly, all the data files would be read and aspects would be extracted from reviews using POS tagging. Specifically words tagged NOUN are considered as aspects. The reason behind considering only them is that a noun is a word that functions as the name of some specific thing or set of things. So, we will get the relevant words based on the domain from the NOUN. Apart from this, a *corpus.txt* also acts as a source for the same. Currently, these aspects are manually defined.

After this, for each review, it analyses the aspect sentiment based on adjectives. Initially, a opinion list is formed by all the words in *pos.txt* and *neg.txt*. Then, for each token in the sentence, we consider only those tokens which are a part of the above token list. For these tokens, we check for tokens with syntactic dependency with this token. Based on the POS that these 'children' belong to (example Verb, Adjective, Conjugation), appropriately sentiment is assigned (please refer code for specific details).

A dictionary object is created for each review, with key as the aspect and value as the sentiment for that particular aspect.

## How to Run?

1) The data should be present in the form of csv's inside a folder titled *main_product*. This should be zipped into *LED_Flashlight.zip* (though the name of the zipped file can be modified in the very first cell in the notebook). <br>
2) The notebook will automatically perform the extraction. After extraction, the input data in the form of csv's will be present. <br>
3) The notebook will automatically create the output and zip it in 'output.zip'. <br>
4) In case of any changes to the format in which data is stored, changes need to be made in sections 1 and 4 accordingly.

## Sample Output
*predictions.csv* contains a sample output for this approach.

## More Information

Spacy Documentation: https://spacy.io/api/token <br>
POS Tagging: https://blog.thaker.ca/linguistics-cheatsheet/ <br>
Medium Article for this approach: https://medium.com/@Intellica.AI/aspect-based-sentiment-analysis-everything-you-wanted-to-know-1be41572e238 <br>
*pos.txt* source: https://gist.github.com/mkulakowski2/4289437 <br>
*neg.txt* source: https://gist.github.com/mkulakowski2/4289441

## Author
Rishabh Karwayun
