#================================================================
# 
#  NLTK: Train NaiveBayesClassifier based on some responses
#  and try to find whether the provide response is 
#  positive or negative
# 
#----------------------------------------------------------------
#
#  Author: Dheeraj Mathur
#  Publish Date: 13 Aug 2015
# 
#================================================================

import nltk

# some positive responses 
positive_responses = [('He is a bright and focussed person', 'positive'),
	('she is confident and cooperative', 'positive'),
	('He is decisive and energetic candidate', 'positive'),
	('He is fine and faithful employee', 'positive'),
	('He is perfect and productive', 'positive'),
    ('He is excellent in the work We recommend this candidate', 'positive'),
    ('She is very punctual and great skillful person', 'positive'),
    ('She has right attitude towards work', 'positive'),
    ('She is very professional and his feedback is positive from our side', 'positive'),
    ('He is very good at his work I suggest you can hire him', 'positive')]

# some negative responses
negative_responses = [('He does not perform well', 'negative'),
	('We fired him for his carelessness', 'negative'),
	('His attitude towards work is not correct', 'negative'),
	('Even after giving warnings, he did not corrected his attitude', 'negative'),
	('He usually gets angry on people', 'negative'),
    ('We cannot recommend this candidate', 'negative'),
    ('He is corrupt and we caught him', 'negative'),
    ('We had to ask him to go back because he was not performing well', 'negative'),
    ('He told us that he is not well and resigned', 'negative'),
    ('She takes so many leaves that is why we had to ask her to give resignation', 'negative'),]

# responses 
responses = []
for (words, sentiment) in positive_responses + negative_responses:
	words_filtered = [e.lower() for e in words.split() if len(e) > 3]
	responses.append((words_filtered, sentiment))

# print responses
# print to see the result


# The list of word features need to be extracted from the responses. It is a list with every distinct words
# ordered by frequency of appearance. We use the following function to get the list plus the two helper
# functions.

def get_words_in_responses(responses):
	all_words = []
	for (words, sentiment) in responses:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_responses(responses))
# print word_features

# To create a classifier, we need to decide what features are relevant. To do that, we first need a
# feature extractor. The one we are going to use returns a dictionary indicating what words are
# contained in the input passed. Here, the input is the response. We use the word features list defined
# above along with the input to create the dictionary.

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features

# We pass the feature extractor along with the responses list defined above.
training_set = nltk.classify.util.apply_features(extract_features, responses)
# print training_set

# The variable training_set contains the labeled feature sets. It is a list of tuples which each tuple
# containing the feature dictionary and the sentiment string for each response. The sentiment string is
# also called label.

classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator=nltk.probability.ELEProbDist):
    # Create the P(label) distribution
    label_probdist = estimator(label_freqdist)
    # Create the P(fval|label, fname) distribution
    feature_probdist = {}
    return NaiveBayesClassifier(label_probdist, feature_probdist)

# show_most_informative_features
# print classifier.show_most_informative_features(32)

response = 'He is a good candidate. He has right attitude towards work. He worked really very hard when he was working with us. He is excellent in what he is doing.'

# print classifier.classify(extract_features(response.split()))

# print extract_features(response.split()), '\n'

print classifier.classify(extract_features(response.split()))


''' NOTE: For some responses, the classifier may not respond correctly.
The reason is that we may not have any information on the feature name.
Larger the training sample responses is, better the classifier will be.'''
