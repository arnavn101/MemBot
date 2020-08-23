from handleRetrieval.retrieve_tweet import RetrieveTweets
from tweepy.error import TweepError as tweetRetrievalError
from utilsFuncs.utils import UtilFunctions


class DataParser:
    def __init__(self, file_path):
        self.file_path = file_path
        UtilFunctions.printClassMethods(self)

    # Microsoft Research Social Media Conversation Corpus Parser
    def parseMRSMConversationCorpus(self):
        file_content = UtilFunctions.retrieveLinesFile(self.file_path)
        finalListConversations = []

        with UtilFunctions.suppressStdout():
            tweet_retriever = RetrieveTweets()
        # 3 tweet conversations per line
        for individual_line in file_content:
            list_conversations = individual_line.split("\t")
            try:
                conversation_1, conversation_2 = tweet_retriever.retrieveTweetId(list_conversations[0]), \
                                                 tweet_retriever.retrieveTweetId(list_conversations[1])
                finalListConversations.append([conversation_1, conversation_2])
                conversation_3 = tweet_retriever.retrieveTweetId(list_conversations[2])
                finalListConversations.append([conversation_2, conversation_3])
            except tweetRetrievalError:
                pass
        return finalListConversations

