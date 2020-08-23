from tweepy import OAuthHandler
import configparser
import os
import sys
import tweepy
from utilsFuncs.utils import UtilFunctions

sys.path.insert(0, os.getcwd())  # Resolve Importing errors


class RetrieveTweets:
    def __init__(self):
        # Get Twitter API Information
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join("config_files", "auth.cfg"))

        # create OAuthHandler object 
        self.auth = OAuthHandler(self.config.get('Twitter', 'consumer_key'),
                                 self.config.get('Twitter', 'consumer_secret'))
        # set access token and secret 
        self.auth.set_access_token(self.config.get('Twitter', 'account_key'),
                                   self.config.get('Twitter', 'account_secret'))
        # create API object to fetch tweets
        self.twitter_api = tweepy.API(self.auth)

        # Print Class Methods
        UtilFunctions.printClassMethods(self)

    # Execute tweet retrieval by Keyword
    def retrieveTweetsKeyWord(self, keyword_search, number_tweets=10, language_tweets="en"):
        list_tweets = []
        fetched_tweets = self.twitter_api.search(q=keyword_search, count=number_tweets, lang=language_tweets)
        for tweet in fetched_tweets:
            text_tweet = UtilFunctions.clean_tweet(tweet.text)
            if tweet.retweet_count > 0:
                if text_tweet not in list_tweets:
                    list_tweets.append(text_tweet)
            else:
                list_tweets.append(text_tweet)
        return list_tweets

    # Execute tweet retrieval by Id
    def retrieveTweetId(self, id_search):
        fetched_tweet = self.twitter_api.get_status(id_search)
        return UtilFunctions.clean_tweet(fetched_tweet.text)
