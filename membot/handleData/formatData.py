from utilsFuncs.utils import UtilFunctions
from vectorizers import VocabularyHandler

"""
Assumption : FormatData.dataFileName has pairs separated by more than 1 newline
"""


class FormatData:
    def __init__(self, dataFileName, **kwargs):
        self.dataFileName = dataFileName
        UtilFunctions.printClassMethods(self)

        self.Conversations = self.retrieveData()
        self.listConversations = self.listFormat()

        self.vectorizer, self.vectorized_sentences = self.vectorizeSentences(kwargs)

    def vectorizeSentences(self, **kwargs):
        vectorizerName = 'vectorsVocabulary'
        for k, v in kwargs.items():
            if k == 'vectorizerName':
                vectorizerName = v
        return getattr(self, vectorizerName)(kwargs)

    def retrieveData(self):
        listConversations = UtilFunctions.retrieveLinesFile(self.dataFileName)
        return list(filter(None, listConversations))

    def listFormat(self):
        cleanConversations = []
        for conversation_1, conversation_2 in list(zip(self.Conversations[0::2], self.Conversations[1::2])):
            cleanConversations.append([UtilFunctions.formatString(conversation_1),
                                       UtilFunctions.formatString(conversation_2)])
        return cleanConversations

    def vectorsVocabulary(self, vocabHandlerName="vectorsVocabulary", occurrenceCount=3, **kwargs):
        for k, v in kwargs.items():
            if k == 'vocabHandlerName':
                vocabHandlerName = v
            if k == 'occurrenceCount':
                occurrenceCount = v

        vocab_handler = VocabularyHandler(vocabHandlerName)
        for conversation_pair in self.listConversations:
            vocab_handler.appendSentence(conversation_pair[0])
            vocab_handler.appendSentence(conversation_pair[1])
        vocab_handler.removeLowOccurrence(occurrenceCount)
        newListConversations = []

        for conversation_pair in self.listConversations:
            conversation_1, conversation_2 = conversation_pair[0], conversation_pair[1]
            removeConversation = False
            for individual_word in conversation_1.split():
                if individual_word not in vocab_handler.wordIndices.keys():
                    removeConversation = True
                    break
            if not removeConversation:
                for individual_word in conversation_2.split():
                    if individual_word not in vocab_handler.wordIndices.keys():
                        removeConversation = True
                        break
            if not removeConversation:
                newListConversations.append(conversation_pair)
        return vocab_handler, newListConversations
