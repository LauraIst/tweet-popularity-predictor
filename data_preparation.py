
# Step 1: Remove tweets not in English (Twitter's language detection did not manage to detect all)
import pandas as pd
from langdetect import detect
df = pd.read_csv("out_per_id2.csv")
for index, row in df.iterrows():
    print(index, row)
# Possible data cleaning steps to consider:
#   Remove special symbols
#   Remove punctuation
#   Remove stop words (only for non-neural models)
#   Stemming/lemmatization

# Data augmentation (feature extraction) steps to consider:
#   Add information on char count, number of words, number of distinct words, emoji, number of hashtags
#       (There is already info on whether the tweet is a retweet)
#   Consider https://pypi.org/project/tweet-preprocessor/ which supports e.g. emoji processing!
#   Calculate the average number of retweets & favorites per user for all their tweets (maybe separately for retweets and original tweets),
#       and add a normalized retweet_count and favorite_count for each tweet
#   Word embeddings: e.g. BOW, Word2Vec and BERT
#       -> for BERT, it could be asked whether the contextualization of the word embeddings makes a difference in training
#           various models for popularity prediction?

# Split dataset into train, validation and test (per model, since they probably require different features):
#   consider e.g. https://stackoverflow.com/questions/38250710/how-to-split-data-into-3-sets-train-validation-and-test
#   This might still be the best option: https://datascience.stackexchange.com/questions/15135/train-test-validation-set-splitting-in-sklearn
#   See more academic guidelines on the split here: https://cs230.stanford.edu/blog/split/
#   Double-check that the sets have the correct type! (Compare with Jan's code)

# Research questions:
#   1. Finding the most accurate model: Can ask specifically about the difference between contextual vs non-contextual word embeddings
#   2. Analysing feature importance: Train some simpler machine learning models and use e.g. sklearn feature_importance
#       https://www.scikit-yb.org/en/latest/api/model_selection/importances.html
