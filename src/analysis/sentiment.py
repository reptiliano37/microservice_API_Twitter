from nltk.corpus import stopwords
from textblob import TextBlob
import re
import nltk
nltk.download('stopwords')


def sentiment_analysis(json_tweet):
    tweet_words, tweet_blob = clean_tweet(json_tweet['text'])

    tweet_blob = TextBlob(str(tweet_blob))
    print("Polaridad del sentimiento: {polarity}".format(polarity=tweet_blob.sentiment.polarity))

    if tweet_blob.sentiment.polarity < 0:
        sentiment = "negative"

    elif tweet_blob.sentiment.polarity == 0:
        sentiment = "neutral"

    else:
        sentiment = "positive"

    print("Sentimiento: {sentiment}".format(sentiment=sentiment))

    json_analaized_tweet = {
        'user': json_tweet['user'],
        'id': json_tweet['id'],
        'text': json_tweet['text'],
        'location': json_tweet['location'],
        'date': json_tweet['date'],
        'followers': json_tweet['followers'],
        'retweets': json_tweet['retweets'],
        'tag_filter': json_tweet['tag_filter'],
        'tweet_words': tweet_words,
        'polarity': tweet_blob.sentiment.polarity,
        'subjectivity': tweet_blob.sentiment.subjectivity,
        'sentiment': sentiment
    }
    return json_analaized_tweet


def clean_tweet(tweet_str):
    """
    Limpia el tweet de emojis y borra las stopwords del tweet,
    :param tweet_str: tweet de tipo string
    :return: list de palabras
    """

    words_tweet = []
    tweet_str = tweet_str.lower()
    print(tweet_str)
    tweet_str = re.sub(r'([^\w]|\d|https)', ' ', tweet_str.strip())
    print(tweet_str)
    emoji_pattern = re.compile("[\U00010000-\U0010ffff"
                               "\U0001F600-\U0001F64F"
                               "\U0001F300-\U0001F5FF"
                               "\U0001F680-\U0001F6FF"
                               "\U0001F1E0-\U0001F1FF]+", flags=re.UNICODE)
    tweet_str = emoji_pattern.sub(r'', tweet_str)
    for word in tweet_str.split(' '):
        if not (word in stopwords.words('spanish')) and not (word in stopwords.words('english')) and not (word == ''):
            if word == 'co' or word == 'rt':
                pass
            else:
                words_tweet.append(word)
    print(words_tweet)

    return words_tweet, tweet_str
