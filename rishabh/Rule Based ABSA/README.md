# ASPECT BASED SENTIMENT ANALYSIS (ABSA) Rule Based Model.

This approach identifies aspects and analysis corresponding sentiment WITHOUT any need of labelled data. At the most a corpus can be provided to ensure that some specific aspects are considered in case not picked up by the POS tagging.

Folder Contents:
1) *asba_ruleBased.ipynb* contains the code.
2) *corpus.txt* contains the corpus of aspects.
3) *pos.txt* and *neg.txt* contain positive and negative sentiment list.


## How to Run?

The code assumes that the data is present in *'LED_Flashlight.zip'* in the same folder as the notebook. The name of the zip folder can be changed in the first cell of the notebook accordingly. The notebook will automatically perform the extraction. After extraction, the input data should be in the format ```main_product/*.csv```.
The notebook will automatically create the output in a zip format in 'output.zip'.
