# Weighted Sentence Level ABSA Pipeline


## Introduction
[Sentence Level ABSA](https://gitlab.com/gide-analytics/author-analysis/absa/-/tree/master/Bo_code/SentenceBasedABSA) breaks down a sentence into smaller chunks based on aspects using text matching and then performs sentiment analysis. An [end to end pipeline](https://gitlab.com/gide-analytics/author-analysis/absa/-/blob/master/Bo_code/SentenceBasedABSA/ABSA%20pipeline.ipynb) takes in all the review data (csv's), breaks each review into aspects, performs sentiment analysis and aggregates all the data aspect wise and presents a final score.

## Weighted Aggregation
While the earlier approach provides a complete end to end solution for ABSA and aggregation, it gives equal weightage to reviews from verified purchases and others. This approach overcomes this shortcoming by scaling down reviews that were not verified purchases. It does so by the following consideration: <br>

1) If an aspect not present in current review proceed to next review. <br>
2) If current review not a verified purchase, scale down the sentiment value by half. <br>
3) If current review is a verified purchase, sentiment value remains unchanged.

## Additional Information
Please refer the [original Sentence Based ABSA documentation](https://gitlab.com/gide-analytics/author-analysis/absa/-/tree/master/Bo_code/SentenceBasedABSA) for more details.

## Author

Rishabh Karwayun.
