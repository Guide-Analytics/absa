# ABSA and Topic Modelling

Aspect Based Sentiment Analysis with incorporation of Knowledge Graph and Topic Modelling 

## Topic Modelling
BERTopic (BERT Topic Modelling)
* Overview: 
    * Topic modelling is an unsupervised machine learning approach that **discovers topics** in a corpus (a list of reviews) and **groups the reviews** into the topics they belong to. ([for more reading](https://monkeylearn.com/blog/introduction-to-topic-modeling/))
    * BERTopic uses embedding from Sentence Transformers for clustering. ([Original repo](https://github.com/MaartenGr/BERTopic))
    * Input: A list of reviews
    * Output: Several groups of reviews and a list of top_n_words (topics) associated with each group
* Algorithm:
    * Create embeddings for each review using Sentence Transformers
    * Reduce dimensionality (UMAP)
    * Cluster reviews (HDBSCAN) 
    * Calculate word importance per topic (TF-IDF)
* Pros:
    * Good results compared to previous methods, such as LDA, LDA2Vec
* Cons:
    * Reviews in one group have the same topic vector
    * A great portion of the text is not clustered

## ABSA 
* Overview: 
    * Aspect based sentiment analysis has two goals: **aspect extraction and aspect sentiment analysis**
    * Input: A list of reviews
    * Output: For each review, aspects discussed in the review and sentiment for each aspect. Note that different reviews could have different aspect vector.

### Approach 1: A supervised approach
* Overview: A supervised approach on the SemEval dataset ([Original repo](https://github.com/thestrox/Aspect-Based-Sentiment-Analysis))
* Aspect Extraction Algorithm: (supervised)
    * Input (features): Term-frequency matrix (Dimension: # of instances * vocabulary size)
    * Output (Target): a matrix that represents whether a review has an aspect (Dimension: # of instances * N, where N is the most common N aspects.)
    * Use traditional classifiers: SVM, NB
* Aspect Sentiment Analysis Algorithm: (supervised)
    * Input (features):  a matrix that represents whether a review has an aspect (Dimension: # of instances * N, where N is the most common N aspects.)
    * Output (Target): a matrix that represents whether a review has a positive/negative/neutral sentiment on an aspect. (Dimension: # of instances * N, where N is the most common N aspects.)  
    * Use traditional classifiers: SVM, NB  
    * Author has 3 classfiers, ie, one positive classifier, one negative classifier, and one neutral classifier.
* Pros:
    * Provides a basic guideline
* Cons:
    * Very poor results: low F1-scores for both stages.
    * Labelling is expensive. Not scalable.

### Approach 2: A rule-based approach
* Overview: A rule-based (no ML) approach ([Original article](https://medium.com/@Intellica.AI/aspect-based-sentiment-analysis-everything-you-wanted-to-know-1be41572e238))
* Algorithms:
    * POS tagging and remove irrelevant words
    * Look for positive/negative adjective
    * Trace down the syntax tree and look for the noun associated with the adjective
    * Look for negation. If found, flip the sentiment.
* Pros:
    * Scalable
    * Decent results
* Cons:
    * Some empty entries
    * Cannot handle sentences with no nouns.

### Approach 3: sentence-level sentiment analysis
* Overview: A combination of rule-based and machine learning approach ([Inspiration](https://thereviewindex.com/us/p/Apple_AirPods_with_Charging_Case_Previous_Model/AZ-US_B01MQWUXZS))
* Algorithms:
    * Manually define aspects (more accurate) and the keywords associated with each aspect
    * Parse the review (by , . ) into sentences.
    * Match a sentence to an aspect if a keyword appears in the sentence.
    * Apply use pre-trained model for sentiment analysis.
* Pros:
    * Scalable
    * Not implemented, but promising
    * A sentence can be mapped to different aspects
* Cons:
    * Cannot handle sentence with opposite sentiments (Ex: good battery and bad screen.)


 
### Aggregation and Normalization (Under discussion)

Example:

|   | Product A1   | Product A2  |
|---|---|---|
|  Aspect 1 | 0.8  | 0.9  |
|  Aspect 2 | 0.5  | 0.6  |

* Aggregation Proposal: 
    * Run ABSA on the product level
    * Aggregate the results using a weighted average (based on the number of reviews) 
    * Ex (Brand aggregation):  Brand A has two products, A1 and A2. For Aspect 1, sentiment scores for A1 and A2 are 0.8 and 0.9. A1 has 40 reviews and A2 has 10 reviews. Then the weighted sentiment score for product A is (0.8* 40 + 0.9 * 10)/(40 + 10)
    * Pros: flexibility, efficiency
    * Cons: may not have enough data

* Normalization Proposal: 
    * Column-wise normalization (standardization) is not recommended
    * We want a consistent metric which compare b/w products, aspects
    * Use thresholds:0~0.5, 0.5~0.9, 0.9~1 (Colormaps)
    * Above (weighted) average, average, below average
    * Display percentiles (ranking)
