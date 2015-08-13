# Sentiment-Analysis-Using-NLTK

For setting up environment, follow following steps:

1. Go to the code directory

2. Create virtual environment using: 
	virtualenv venv_nlp

3. Activate virtal environment using following:
	. venv_nlp/bin/activate

4. Install requirements:
	pip install -r requirements.txt

5. Download NLTK data
	python -m nltk.downloader all

6. Add following to your .bashrc file
	export NLTK_DATA="< path to nltk_data >"

7. Open sentiment_analysis.py file and change value of response variable at Line 100 to your value

8. Run program using following command:
	python sentiment_analysis.py

	
It will return whether the response is positive or negative. 

Note: 

There are multiple print statements which are commented, you can uncomment these to check intermediate values as well.  

To train NaiveBayesClassifier there are few positive_responses and negative_responses are written, These are very important to produce correct result. In my case I have added responses for NaiveBayesClassifier trainig which denotes response of a hr. If your context is different you can update these positive_responses and negative_responses to get accurate result. 

Larger the training sample responses is, better the classifier will be.

For production use, we can take these inputs from database along with polarity is already assigned. With the number of sample inputs accuracy of the system will increase. 